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

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="admin",
            email="admin@admin.com",
            password="superadmin",
            first_name="test",
            last_name="user",
        )


class GetAllOrdersTest(BaseViewTest):
    def setUp(self):
        self.valid_payload = {
            'name': 'Muffin',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }

    def test_get_all_orders(self):
        # fetch the data from db
        expected = Order.objects.all()
        serialized = OrderSerializer(expected, many=True)

        # hit api
        response = client.get(reverse('orders-all', kwargs={"version": "v1"}))

        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetDetailOrderTest(BaseViewTest):
    def test_get_detail_order(self):
        expected = Order.objects.get(pk=1)
        serialized = OrderSerializer(expected, many=True)

        response = client.get(reverse('get_detail_order'))

        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# class DeleteOrderTest(TestCase):
#     def test_delete_order(self):
#         response = client.delete(reverse('get_detail_order'))

#         # self.assertEqual(response.data, serialized.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class CreateOrderTest(TestCase):
#     def test_create_order(self):
#         response = client.post(reverse('get_detail_order'))

#         # self.assertEqual(response.data, serialized.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class UpdateOrderTest(TestCase):
#     def test_create_order(self):
#         response = client.put(reverse('get_detail_order'))

#         # self.assertEqual(response.data, serialized.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

class AuthLoginTest(BaseViewTest):
    def test_valid_login_user(self):
        response = self.login("admin", "superadmin")
        self.assertIn("token", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
