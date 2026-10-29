from django.db import models

class Brand(models.Model):
    name = models.CharField("Марка", max_length=80, unique=True)
    country = models.CharField("Страна", max_length=80, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Марка"
        verbose_name_plural = "Марки"
        ordering = ["name"]
    def __str__(self):
        return self.name

class Car(models.Model):
    class FuelType(models.TextChoices):
        PETROL = "petrol", "Бензин"
        DIESEL = "diesel", "Дизель"
        ELECTRIC = "electric", "Электро"
        HYBRID = "hybrid", "Гибрид"

    class Status(models.TextChoices):
        AVAILABLE = "available", "В наличии"
        RESERVED = "reserved", "Зарезервирован"
        SOLD = "sold", "Продан"
        SERVICE = "service", "На обслуживании"

    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="cars", verbose_name="Марка")
    model = models.CharField("Модель", max_length=100)
    year = models.PositiveSmallIntegerField("Год выпуска")
    price = models.DecimalField("Цена", max_digits=12, decimal_places=2)
    color = models.CharField("Цвет", max_length=40, blank=True)
    engine_volume = models.DecimalField("Объём двигателя, л", max_digits=3, decimal_places=1,
                                        null=True, blank=True)
    fuel_type = models.CharField("Тип топлива", max_length=20, choices=FuelType.choices, default=FuelType.PETROL)
    mileage = models.PositiveIntegerField("Пробег, км", default=0)
    status = models.CharField("Статус", max_length=20, choices=Status.choices, default=Status.AVAILABLE)
    vin = models.CharField("VIN", max_length=32, unique=True)
    description = models.TextField("Описание", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"
        ordering = ["-created_at"]
    def __str__(self):
        return f"{self.brand.name} {self.model} ({self.year})"
