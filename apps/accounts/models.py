from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Position(models.TextChoices):
        ADMIN = "admin", "Администратор"
        MANAGER = "manager", "Менеджер"
        DIRECTOR = "director", "Директор"

    phone = models.CharField("Телефон", max_length=20, blank=True)
    position = models.CharField("Должность", max_length=20, choices=Position.choices,
                                default=Position.MANAGER)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ["username"]

    def __str__(self):
        return self.get_full_name() or self.username
