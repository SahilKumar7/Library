from turtle import title
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13, verbose_name="ISBN")

    def __str__(self):
        return self.title