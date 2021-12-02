from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import *

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("id", "created_at", "author", "url", "topic", "body", "parent")


class NoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("topic", "body", "parent")


class NoteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("id", "created_at", "topic", "body", "parent")
        read_only_fields = ("id", "created_at", "parent")


#
#
