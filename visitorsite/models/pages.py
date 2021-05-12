from django.db import models
from django.db.models.fields import CharField

class Page(models.Model):
    title=models.CharField(verbose_name="Page Title", max_length=250)
    slug=models.CharField(verbose_name="Page's URL Slug'", max_length=250)

    def __str__(self):
        return self.title