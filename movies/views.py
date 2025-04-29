"""Views for the Movies app."""

from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieModelSerializer, MovieListDetailSerializer
from app.permissions import GlobalDefaultPermission
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    """View for listing and creating movies."""
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting a movie."""
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieStatsView(views.APIView):
    """View for retrieving movie statistics."""
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get(self, request):
        """Handle GET requests to retrieve movie statistics."""
        total_movies = self.queryset.count()
        movie_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(average_stars=Avg('stars'))['average_stars']

        return response.Response(
            data={'message': 'Success',
                  'total_movies': total_movies,
                  'movie_by_genre': movie_by_genre,
                  'total_reviews': total_reviews,
                  'average_stars': round(average_stars, 1) if average_stars else 0,
                  },
            status=status.HTTP_200_OK,
        )
