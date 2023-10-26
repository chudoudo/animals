from django.db import models

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=40)
    breed = models.CharField(max_length=40)

