from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "car", "manager", "order_type", "status", "price", "created_at")
    list_filter = ("status", "order_type", "created_at")
    search_fields = ("client__full_name", "car__model", "car__brand__name")
    list_editable = ("status",)
