from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Category, Ticket

class TicketApiTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="tester", password="test-password-123", role="requester")
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.category = Category.objects.create(name="Тестовая категория")

    def test_authenticated_user_can_create_ticket(self):
        response = self.client.post("/api/tickets/", {
            "title": "Тестовая заявка",
            "description": "Проверка создания обращения",
            "category": self.category.id,
            "priority": "medium",
        }, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Ticket.objects.count(), 1)
        self.assertEqual(Ticket.objects.first().requester, self.user)

    def test_health_endpoint_is_public(self):
        response = self.client.get("/api/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], "ok")
