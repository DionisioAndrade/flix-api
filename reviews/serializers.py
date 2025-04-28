"""Module for actors Serializers in the API-Flix."""

from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for the Review model. Converts Review instances into JSON format."""

    class Meta:
        model = Review
        fields = '__all__'
