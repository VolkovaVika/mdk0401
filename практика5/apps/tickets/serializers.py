from rest_framework import serializers
from .models import Ticket, Category, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description", "is_active"]

class TicketSerializer(serializers.ModelSerializer):
    requester_name = serializers.CharField(source="requester.username", read_only=True)
    assignee_name = serializers.CharField(source="assignee.username", read_only=True)
    category_name = serializers.CharField(source="category.name", read_only=True)
    status_display = serializers.CharField(source="get_status_display", read_only=True)
    priority_display = serializers.CharField(source="get_priority_display", read_only=True)

    class Meta:
        model = Ticket
        fields = [
            "id", "title", "description", "requester", "requester_name", "assignee",
            "assignee_name", "category", "category_name", "status", "status_display",
            "priority", "priority_display", "created_at", "updated_at", "resolved_at"
        ]
        read_only_fields = ["id", "requester", "created_at", "updated_at", "resolved_at"]

    def create(self, validated_data):
        validated_data["requester"] = self.context["request"].user
        return super().create(validated_data)

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.username", read_only=True)
    class Meta:
        model = Comment
        fields = ["id", "ticket", "author", "author_name", "text", "created_at"]
        read_only_fields = ["id", "author", "created_at"]

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)
