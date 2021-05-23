from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from parser_books.models import Book


class Profile(models.Model):
    """custom user class"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Chain to user class for modify him")
    books = models.ManyToManyField(Book, verbose_name="User books")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()