from django.db import models


class Book(models.Model):
    """class for book"""
    name = models.TextField(verbose_name="Title of book")
    author = models.TextField(verbose_name="Author of book")
    description = models.TextField(verbose_name="Description of book")
    img_link = models.URLField(verbose_name="Link of book cover")
    link = models.URLField(unique=True, verbose_name="Link to book")
    download_link = models.URLField(verbose_name="Link to download book")
