from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ["id", "username", "email", "phone", "position", "full_name"]
        read_only_fields = ["id"]

    def get_full_name(self, obj):
        return obj.get_full_name()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    full_name = serializers.CharField(write_only=True, required=False, allow_blank=True)
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "phone", "position", "full_name"]

    def create(self, validated_data):
        full_name = validated_data.pop("full_name", "")
        parts = full_name.strip().split()
        user = User(**validated_data)
        user.first_name = parts[0] if parts else ""
        user.last_name = " ".join(parts[1:]) if len(parts) > 1 else ""
        user.set_password(validated_data["password"])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    def validate(self, attrs):
        user = authenticate(username=attrs.get("username"), password=attrs.get("password"))
        if not user:
            raise serializers.ValidationError("Неверное имя пользователя или пароль.")
        if not user.is_active:
            raise serializers.ValidationError("Учётная запись отключена.")
        attrs["user"] = user
        return attrs
