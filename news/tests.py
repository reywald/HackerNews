from django.http import response
from django.test import TestCase

# Create your tests here.
class HomePageViewTest(TestCase):

    def setUp(self) -> None:
        pass

    def test_api_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
