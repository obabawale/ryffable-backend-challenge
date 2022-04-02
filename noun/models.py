from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Animal(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Food(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Thing(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Noun(models.Model):
    name = models.CharField(max_length=64)
    place = models.ForeignKey(Place,  on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal,  on_delete=models.CASCADE)
    food = models.ForeignKey(Food,  on_delete=models.CASCADE)
    things = models.ManyToManyField(Thing)

    def __str__(self) -> str:
        return f"{self.name}"