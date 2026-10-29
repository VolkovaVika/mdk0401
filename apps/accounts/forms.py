from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Имя пользователя"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "Пароль"}))

class RegisterForm(UserCreationForm):
    full_name = forms.CharField(label="ФИО", max_length=150, required=True)
    email = forms.EmailField(label="Email", required=True)
    phone = forms.CharField(label="Телефон", max_length=20, required=False)
    position = forms.ChoiceField(label="Должность", choices=User.Position.choices)

    class Meta:
        model = User
        fields = ("username", "full_name", "email", "phone", "position", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        parts = self.cleaned_data["full_name"].strip().split()
        user.first_name = parts[0] if parts else ""
        user.last_name = " ".join(parts[1:]) if len(parts) > 1 else ""
        user.email = self.cleaned_data["email"]
        user.phone = self.cleaned_data["phone"]
        user.position = self.cleaned_data["position"]
        if commit:
            user.save()
        return user
