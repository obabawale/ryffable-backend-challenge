from .models import Noun
from rest_framework import viewsets
from noun.serializers import NounSerializer


class NounViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows nouns to be viewed or edited.
    """
    queryset = Noun.objects.all().order_by('-name')
    serializer_class = NounSerializer
