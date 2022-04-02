from .models import Noun, Place, Animal, Thing, Food
from rest_framework import serializers


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'url', 'name']


class ThingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Thing
        fields = ['id', 'url', 'name']


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'url', 'name']


class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'url', 'name']


class NounSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Noun
        fields = ['id', 'url', 'name', 'place', 'animal', 'food', 'things']