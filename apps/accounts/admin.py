from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Рабочие данные", {"fields": ("phone", "position")}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Рабочие данные", {"fields": ("phone", "position")}),)
    list_display = ("username", "email", "first_name", "last_name", "position", "is_staff")
    list_filter = ("position", "is_staff", "is_active")
