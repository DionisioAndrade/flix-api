from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieModelSerializer

class MovieCreateListView(generics.ListCreateAPIView):
    """View for listing and creating movies."""
    
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    
class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting a movie."""
    
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer