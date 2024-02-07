# tests/test_views.py

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(name="Test Item 1", price=10.99, description="Test Description 1")
        Menu.objects.create(name="Test Item 2", price=15.99, description="Test Description 2")

    def test_getall(self):
        # Retrieve all Menu objects added for the test purpose
        client = APIClient()
        url = reverse('menu-list')  # Assuming you have a 'menu-list' endpoint configured in your URLs
        response = client.get(url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Assert if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert if the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)
