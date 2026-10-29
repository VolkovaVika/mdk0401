from django.contrib import admin
from .models import Ticket, Category, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "requester", "assignee", "category", "status", "priority", "created_at")
    list_filter = ("status", "priority", "category", "created_at")
    search_fields = ("title", "description", "requester__username", "assignee__username")
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "created_at"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "ticket", "author", "created_at")
    search_fields = ("text", "ticket__title", "author__username")
