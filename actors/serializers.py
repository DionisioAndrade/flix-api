"""Module for actors Serializers in the API-Flix."""

from rest_framework import serializers
from actors.models import Actor

class ActorSerializer(serializers.ModelSerializer):
    """Serializer for the Actor model. Converts Actor instances into JSON format."""

    class Meta:
        model = Actor
        fields = '__all__'
