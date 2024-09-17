# members/tests.py
from django.test import TestCase, Client
from django.urls import reverse
import json

class MyViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello_view_without_name(self):
        response = self.client.get(reverse('hello_view'))
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data['greeting'], "Hello, World")

    def test_hello_view_with_name(self):
        response = self.client.get(reverse('hello_view') + '?name=John')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data['greeting'], "Hello, John")
    
    def test_info_view(self):
        response = self.client.get(reverse('info_view'))
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertIn('time', response_data)
        self.assertIn('client_address', response_data)
        self.assertIn('host_name', response_data)
        self.assertIn('headers', response_data)
