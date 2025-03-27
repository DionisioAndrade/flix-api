"""Views for the Actor app."""

from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorCreateListView(generics.ListCreateAPIView):
    """Handles creating and listing actors."""
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Handles retrieving, updating, and deleting actors."""
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    