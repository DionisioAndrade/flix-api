"""Module for genre serializers in the API-Flix."""

from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    """Serializer for the Movie model. Converts Movie instances into JSON format."""
    
    class Meta:
        model = Movie
        fields= '__all__'