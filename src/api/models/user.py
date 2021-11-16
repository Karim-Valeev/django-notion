from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager as DjangoUserManager
from django.db import models

from .base import BaseModel


class UserManager(DjangoUserManager):
    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.model(email=email, is_superuser=True)
        user.set_password(password)
        user.save()
        return user


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    # Чтобы модель работала нормально нужно для нее переопределить UserManager
    objects = UserManager()

    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "profile"
        verbose_name = "User"
        verbose_name_plural = "Users"
