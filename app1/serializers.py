from djoser.serializers import UserCreateSerializer
from .models import CustomUser
from rest_framework.serializers import ModelSerializer


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ("id", "email", "username", "password")

