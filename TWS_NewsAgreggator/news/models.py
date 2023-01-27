from os import link
from turtle import title
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)
    link = models.CharField(max_length=200)


    def __str__(self):
        return self.title
 