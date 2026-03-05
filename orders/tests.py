from django.test import TestCase
from rest_framework.test import APITestCase
from here.models import Restaurant


class RestaurantInfoAPITestCase(APITestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name = "Test Restaurant" ,
            address="123 Test St"
        )
    def test_get_restaurant_info(self):
        response = self.client.get('/api/restaurant-info/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], self.restaurant.name)
        self.assertEqual(response.data['address'], self.restaurant.address)