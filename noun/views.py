from .models import Noun, Place, Animal, Food, Thing
from rest_framework import viewsets
from noun.serializers import NounSerializer, PlaceSerializer, AnimalSerializer, FoodSerializer, ThingSerializer
from rest_framework import filters


class FoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows foods to be viewed or edited.
    """
    queryset = Food.objects.all().order_by('id')
    serializer_class = FoodSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['name']


class ThingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows things to be viewed or edited.
    """
    queryset = Thing.objects.all().order_by('id')
    serializer_class = ThingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['name']


class AnimalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows animals to be viewed or edited.
    """
    queryset = Animal.objects.all().order_by('id')
    serializer_class = AnimalSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['name']


class PlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows nouns to be viewed or edited.
    """
    queryset = Place.objects.all().order_by('id')
    serializer_class = PlaceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['name']


class NounViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows nouns to be viewed or edited.
    """
    queryset = Noun.objects.all().order_by('id')
    serializer_class = NounSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'place__name', 'animal__name', 'food__name', 'things__name']
    filterset_fields = ['name']
    ordering_fields = ['name', 'animal', 'things']
    ordering = ['name']
