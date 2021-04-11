from django.db import models


class User(models.Model):
    """model for user"""
    id = models.PositiveIntegerField(primary_key=True, verbose_name="Unique id for user")
    email = models.EmailField(verbose_name="User email")
    password = models.TextField(verbose_name="User password")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
