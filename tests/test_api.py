from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from apps.accounts.models import User
from apps.catalog.models import Brand, Car

class BasicApiTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="manager", password="StrongPass123!")
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_brands_endpoint(self):
        Brand.objects.create(name="Toyota", country="Japan")
        response = self.client.get("/api/brands/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(x["name"] == "Toyota" for x in response.data))

    def test_car_endpoint(self):
        brand = Brand.objects.create(name="Volvo", country="Sweden")
        Car.objects.create(brand=brand, model="XC60", year=2023, price="35000.00", vin="TESTVIN0001")
        response = self.client.get("/api/cars/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["results"][0]["model"], "XC60") if isinstance(response.data, dict) and "results" in response.data else self.assertTrue(response.data)
