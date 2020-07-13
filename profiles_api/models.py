from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


# Database Models for users in system
class UserProfile(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    

