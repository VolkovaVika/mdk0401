from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        REQUESTER = "requester", "Заявитель"
        OPERATOR = "operator", "Оператор"
        AGENT = "agent", "Исполнитель"
        ADMIN = "admin", "Администратор"

    role = models.CharField("Роль", max_length=20, choices=Role.choices, default=Role.REQUESTER)
    department = models.CharField("Подразделение", max_length=120, blank=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_role_display()})"
