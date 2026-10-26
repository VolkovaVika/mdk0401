from django.db import models

class Location(models.Model):
    name = models.CharField("Название местоположения", max_length=150, unique=True)
    address = models.CharField("Адрес", max_length=255, blank=True)

    class Meta:
        verbose_name = "местоположение"
        verbose_name_plural = "местоположения"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField("Название категории", max_length=120, unique=True)
    description = models.TextField("Описание", blank=True)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField("Название производителя", max_length=150, unique=True)
    website = models.URLField("Сайт", blank=True)

    class Meta:
        verbose_name = "производитель"
        verbose_name_plural = "производители"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField("Название модели", max_length=150)
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT, related_name="models", verbose_name="Производитель")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="models", verbose_name="Категория")

    class Meta:
        verbose_name = "модель"
        verbose_name_plural = "модели"
        ordering = ["vendor__name", "name"]
        constraints = [models.UniqueConstraint(fields=["vendor", "name"], name="unique_vendor_model_name")]

    def __str__(self):
        return f"{self.vendor} — {self.name}"
