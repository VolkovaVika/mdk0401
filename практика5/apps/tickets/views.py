from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Ticket, Category, Comment
from .serializers import TicketSerializer, CategorySerializer, CommentSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.select_related("requester", "assignee", "category").all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ["status", "priority", "category", "assignee", "requester"]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "updated_at", "priority", "status"]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ["name"]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("ticket", "author").all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ["ticket", "author"]
