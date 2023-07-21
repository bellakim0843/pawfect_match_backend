from rest_framework.serializers import ModelSerializer
from .models import User


class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "is_sitter",
            "username",
        )


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "last_login",
            "username",
            "name",
            "is_sitter",
        )


class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )
