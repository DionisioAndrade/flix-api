"""Module for genre serializers in the API-Flix."""

from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from actors.models import Actor
import datetime


class MovieSerializer(serializers.Serializer):
    """Serializer for the Movie . Converts Movie instances into JSON format."""
    id = serializers.IntegerField(
        read_only=True
    )
    title = serializers.CharField()
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all()
    )
    release_date = serializers.DateField()
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True,
    )
    resume = serializers.CharField()


class MovieModelSerializer(serializers.ModelSerializer):
    """Serializer for the Movie model. Converts Movie instances into JSON format."""

    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        """Calculates the average rate of the movie."""
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        return None

    def validate_release_date(self, value):
        """Validates the release date of the movie."""
        if value.year > datetime.datetime.now().year:
            raise serializers.ValidationError("The release date cannot be in the future.")
        return value

    def validate_resume(self, value):
        """Validates the resume of the movie."""
        if len(value) > 500:
            raise serializers.ValidationError("The resume cannot be longer than 500 characters.")
        return value
