from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# # Create your models here.
# class Users(models.Model):
#     username = models.CharField(max_length=150, unique=True)
#     email = models.EmailField(max_length=255, unique=True)
#     password = models.CharField(max_length=128)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30, blank=True)
#     likes = models.PositiveIntegerField(default=0)
#     dislikes = models.PositiveIntegerField(default=0)
#     summary = models.TextField(blank=True)
#     age = models.PositiveIntegerField(blank=True, null=True)
#     active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f"{self.username}"

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    # Add your custom fields here
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    summary = models.TextField(blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

    # Provide unique related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',  # Use a unique name
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users_permissions',  # Use a unique name
        blank=True,
    )
