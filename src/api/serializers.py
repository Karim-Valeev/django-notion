# from django.contrib.auth import get_user_model
# from rest_framework import serializers
#
# from .models import Basket, Status
#
# User = get_user_model()
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email')
#
#
# class StatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Status
#         fields = ('code', 'name')
#
#
# class BasketCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Basket
#         fields = ('name', 'delivery_address', 'favourite')
#
#
# class BasketUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Basket
#         fields = ('id', 'created_at', 'name', 'delivery_address', 'favourite')
#         read_only_fields = ('id', 'created_at', )
#
#
# class BasketSerializer(serializers.ModelSerializer):
#     owner = UserSerializer()
#     status = StatusSerializer()
#
#     class Meta:
#         model = Basket
#         fields = ('id', 'created_at', 'name',
#                   'delivery_address', 'favourite', 'status',
#                   'owner')
