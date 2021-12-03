from django.test import TestCase
from django.test import Client
# Create your tests here.
from django.urls import reverse


class HealthcheckTestCase(TestCase):
    client = Client()
    def test_status_response(self):
        response =self.client.get(
            reverse('check_status')
        )

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content , b"OK!")

