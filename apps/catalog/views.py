from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Brand, Car
from .serializers import BrandSerializer, CarSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "country"]
    ordering_fields = ["name", "created_at"]

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.select_related("brand").all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ["brand__name", "model", "vin", "color"]
    filterset_fields = ["brand", "year", "fuel_type", "status"]
    ordering_fields = ["year", "price", "mileage", "created_at"]
