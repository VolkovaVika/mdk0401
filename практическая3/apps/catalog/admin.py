from django.contrib import admin
from .models import Location, Category, Vendor, Model

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    search_fields = ("name", "address")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ("name", "website")
    search_fields = ("name",)

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ("name", "vendor", "category")
    list_filter = ("vendor", "category")
    search_fields = ("name", "vendor__name", "category__name")
