from django.db import models

# Create your models here.
class Noun(models.Model):
    name = models.CharField(max_length=64)
    place = models.CharField(max_length=64)
    animal = models.CharField(max_length=64)
    food = models.CharField(max_length=64)
    things = models.CharField(max_length=64)