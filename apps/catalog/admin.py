from django.contrib import admin
from .models import Brand, Car

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "created_at")
    search_fields = ("name", "country")

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "year", "price", "status", "vin")
    list_filter = ("status", "fuel_type", "brand", "year")
    search_fields = ("brand__name", "model", "vin")
    list_editable = ("status",)
