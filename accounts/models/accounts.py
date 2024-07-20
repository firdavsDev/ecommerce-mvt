from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from ..managers import CustomUserManager


class CustomUser(AbstractUser, PermissionsMixin):
    """
    Custom user model
    """

    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}"

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
