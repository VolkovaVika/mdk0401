from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["full_name", "phone", "email", "passport", "birth_date", "manager"]
        widgets = {"birth_date": forms.DateInput(attrs={"type": "date"})}
