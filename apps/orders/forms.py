from django import forms
from .models import Order
from apps.catalog.models import Car

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["client", "car", "manager", "order_type", "status", "price", "notes"]
        widgets = {"notes": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["car"].queryset = Car.objects.exclude(status=Car.Status.SOLD)
