from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related("client", "car", "car__brand", "manager").all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["client__full_name", "car__model", "car__brand__name"]
    ordering_fields = ["created_at", "price", "status"]
