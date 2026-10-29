from django.conf import settings
from django.db import models, transaction
from django.core.exceptions import ValidationError
from apps.catalog.models import Car
from apps.clients.models import Client

class Order(models.Model):
    class OrderType(models.TextChoices):
        SALE = "sale", "Продажа"
        RESERVATION = "reservation", "Бронирование"

    class Status(models.TextChoices):
        NEW = "new", "Новый"
        IN_PROGRESS = "in_progress", "В работе"
        COMPLETED = "completed", "Завершён"
        CANCELLED = "cancelled", "Отменён"

    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name="orders", verbose_name="Клиент")
    car = models.ForeignKey(Car, on_delete=models.PROTECT, related_name="orders", verbose_name="Автомобиль")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
                                 related_name="orders", verbose_name="Менеджер")
    order_type = models.CharField("Тип заказа", max_length=20, choices=OrderType.choices, default=OrderType.SALE)
    status = models.CharField("Статус", max_length=20, choices=Status.choices, default=Status.NEW)
    price = models.DecimalField("Цена сделки", max_digits=12, decimal_places=2)
    notes = models.TextField("Комментарий", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField("Дата завершения", null=True, blank=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Заказ #{self.pk}: {self.client} — {self.car}"

    def clean(self):
        if self.car_id and self.status not in [self.Status.CANCELLED] and self.car.status == Car.Status.SOLD and self.pk is None:
            raise ValidationError({"car": "Этот автомобиль уже продан."})

    @transaction.atomic
    def save(self, *args, **kwargs):
        from django.utils import timezone
        self.full_clean(exclude=None)
        if self.status == self.Status.COMPLETED and not self.completed_at:
            self.completed_at = timezone.now()
        super().save(*args, **kwargs)
        car = self.car
        if self.status == self.Status.COMPLETED and self.order_type == self.OrderType.SALE:
            car.status = Car.Status.SOLD
            car.save(update_fields=["status"])
        elif self.status == self.Status.CANCELLED and car.status == Car.Status.RESERVED:
            car.status = Car.Status.AVAILABLE
            car.save(update_fields=["status"])
        elif self.order_type == self.OrderType.RESERVATION and self.status in [self.Status.NEW, self.Status.IN_PROGRESS]:
            if car.status == Car.Status.AVAILABLE:
                car.status = Car.Status.RESERVED
                car.save(update_fields=["status"])
