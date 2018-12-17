import json

from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from order.models import Order
from order.serializers import OrderSerializer
from django.contrib.auth.models import User
# Create your tests here.


class BaseViewTest(APITestCase):
    client = APIClient()

    def login(self, username="", password=""):
        url = reverse(
            "create-token"
        )
        return self.client.post(
            url,
            data=json.dumps({
                "username": username,
                "password": password
            }),
            content_type="application/json"
        )

    def login_user(self, username="", password=""):
        response = self.login(username, password)

        self.token = response.data['token']
        # set the token in the header
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.token
        )
        self.client.login(username=username, password=password)
        return self.token

    def get_order_list(self):
        return self.client.get(
            reverse(
                "order-list-create",
                kwargs={
                    "version": "v1"
                }
            )
        )

    def get_order_detail(self, pk=0):
        return self.client.get(self.order_url(pk))

    def delete_order(self, pk=0):
        return self.client.delete(self.order_url(pk))

    def update_order_detail(self, pk=0):
        return self.client.put(self.order_url(pk))

    def order_url(self, pk=0):
        url = reverse(
            "order-delete-update-show",
            kwargs={
                "version": "v1",
                "pk": pk
            }
        )
        return url

    def create_order(self, size='M', user=""):
        Order.objects.create(size=size, user=user)

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="admin",
            email="admin@admin.com",
            password="superadmin",
            first_name="test",
            last_name="user",
        )

        self.create_order('XL', self.user)
        # self.create_order('M', self.user)

        self.new_order = {'size': 'XXL'}


class GetAllOrdersTest(BaseViewTest):
    def test_get_all_orders(self):
        # fetch the data from db
        expected = Order.objects.all()
        serialized = OrderSerializer(expected, many=True)

        # hit api
        self.login_user(self.user.username, 'superadmin')
        response = self.get_order_list()

        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetDetailOrderTest(BaseViewTest):
    def test_get_detail_order(self):
        expected = Order.objects.get(pk=1)
        serialized = OrderSerializer(expected)

        self.login_user(self.user.username, 'superadmin')
        response = self.get_order_detail(1)

        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteOrderTest(BaseViewTest):
    def test_delete_order(self):
        self.login_user(self.user.username, 'superadmin')
        response = self.delete_order(pk=1)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)


class UpdateOrderTest(BaseViewTest):
    def test_update_order(self):
        self.login_user(self.user.username, 'superadmin')
        response = self.client.put(reverse(
            "order-delete-update-show",
            kwargs={
                "version": 'v1',
                "pk": 1
            }
        ),
            data=json.dumps(self.new_order),
            content_type='application/json'
        )

        self.assertEqual(response.data['size'], self.new_order['size'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateOrderTest(BaseViewTest):
    def test_create_order(self):
        self.login_user(self.user.username, 'superadmin')
        response = self.client.post(reverse(
            "order-list-create",
            kwargs={"version": 'v1', }
        ),
            data=json.dumps(self.new_order),
            content_type='application/json'
        )

        self.assertEqual(response.data['size'], self.new_order['size'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class AuthLoginTest(BaseViewTest):
    def test_valid_login_user(self):
        response = self.login("admin", "superadmin")
        self.assertIn("token", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
