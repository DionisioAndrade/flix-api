"""Views for the Movies app."""

from rest_framework import generics
from rest_framework.authentication import isAuthenticated
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieModelSerializer

class MovieCreateListView(generics.ListCreateAPIView):
    """View for listing and creating movies."""
    authentication_classes = (isAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    
class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting a movie."""
    authentication_classes = (isAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer