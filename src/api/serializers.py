from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import *

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id",)


class NoteSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Note
        fields = ("id", "created_at", "author", "url", "topic", "body", "parent")


class NoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        # author и url будут сами проставляться
        fields = ("topic", "body", "parent")


class NoteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("id", "created_at", "topic", "body", "parent")
        read_only_fields = ("id", "created_at", "parent")


#
#
