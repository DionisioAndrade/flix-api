"""Module for genre serializers in the API-Flix."""

import datetime
from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from actors.models import Actor
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


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


class MovieListDetailSerializer(serializers.ModelSerializer):
    """Serializer for the Movie model. Converts Movie instances into JSON format. just method GET"""
    genre = GenreSerializer()
    actors = ActorSerializer(many=True)
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        """Calculates the average rate of the movie."""
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        return None


class MovieModelSerializer(serializers.ModelSerializer):
    """Serializer for the Movie model. Converts Movie instances into JSON format. just method POST"""
    class Meta:
        model = Movie
        fields = '__all__'

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
