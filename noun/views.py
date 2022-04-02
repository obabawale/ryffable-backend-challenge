from .models import Noun, Place, Animal, Food, Thing
from rest_framework import viewsets
from noun.serializers import NounSerializer, PlaceSerializer, AnimalSerializer, FoodSerializer, ThingSerializer


class FoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows foods to be viewed or edited.
    """
    queryset = Food.objects.all().order_by('id')
    serializer_class = FoodSerializer


class ThingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows things to be viewed or edited.
    """
    queryset = Thing.objects.all().order_by('id')
    serializer_class = ThingSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows animals to be viewed or edited.
    """
    queryset = Animal.objects.all().order_by('id')
    serializer_class = AnimalSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows nouns to be viewed or edited.
    """
    queryset = Place.objects.all().order_by('id')
    serializer_class = PlaceSerializer


class NounViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows nouns to be viewed or edited.
    """
    queryset = Noun.objects.all().order_by('id')
    serializer_class = NounSerializer
