from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Пользователь системы с необязательным номером телефона."""
    phone = models.CharField("Телефон", max_length=20, blank=True)

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.get_full_name() or self.username
