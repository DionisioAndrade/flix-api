"""Module for genre serializers in the API-Flix."""

from rest_framework import serializers
from genres.models import Genre

class GenreSerializer(serializers.ModelSerializer):
    """Serializer for the Genre model. Converts Actor instances into JSON format."""
    
    class Meta:
        model = Genre
        fields= '__all__'
