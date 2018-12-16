import json

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from order.serializers import OrderSerializer


client = Client()
# Create your tests here.


class OrdersTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'name': 'Muffin',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }

    def test_get_all_orders(self):
        response = client.get(reverse('get_all_order'))
        self.assertEqual(response.status_code, status)

    def test_store_order(self):
        response = client.post(
            reverse('get_all_order'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
