from django.db import models


class Book(models.Model):
    name = models.TextField()
    author = models.TextField()
    description = models.TextField()
    img_link = models.URLField()
    link = models.URLField()
    download_link = models.URLField()
