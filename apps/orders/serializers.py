from rest_framework import serializers
from .models import Order
from apps.catalog.models import Car

class OrderSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source="client.full_name", read_only=True)
    car_name = serializers.CharField(source="car.__str__", read_only=True)
    manager_name = serializers.CharField(source="manager.get_full_name", read_only=True)
    status_display = serializers.CharField(source="get_status_display", read_only=True)
    class Meta:
        model = Order
        fields = ["id", "client", "client_name", "car", "car_name", "manager", "manager_name",
                  "order_type", "status", "status_display", "price", "notes", "created_at", "completed_at"]
        read_only_fields = ["id", "created_at", "completed_at"]

    def validate(self, attrs):
        car = attrs.get("car", getattr(self.instance, "car", None))
        status = attrs.get("status", getattr(self.instance, "status", Order.Status.NEW))
        if car and car.status == Car.Status.SOLD and status != Order.Status.CANCELLED:
            raise serializers.ValidationError({"car": "Этот автомобиль уже продан."})
        return attrs
