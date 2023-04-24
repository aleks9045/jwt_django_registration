from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from .models import CustomUser


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ("id", "email", "username", "password")
