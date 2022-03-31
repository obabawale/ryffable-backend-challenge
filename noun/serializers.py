from .models import Noun
from rest_framework import serializers


class NounSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Noun
        fields = ['name', 'place', 'animal', 'food', 'things']