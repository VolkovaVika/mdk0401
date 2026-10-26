from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Дополнительная информация", {"fields": ("phone",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Дополнительная информация", {"fields": ("phone",)}),)
    list_display = ("username", "first_name", "last_name", "email", "phone", "is_staff")
    search_fields = ("username", "first_name", "last_name", "email", "phone")
