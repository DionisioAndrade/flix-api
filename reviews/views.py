"""Views for the Review app."""

from rest_framework import generics
from rest_framework.authentication import isAuthenticated
from reviews.models import Review
from reviews.serializers import ReviewSerializer

class ReviewListCreateView(generics.ListCreateAPIView):
    """Handles creating and listing Review."""
    authentication_classes = (isAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Handles retrieving, updating, and deleting Review."""
    authentication_classes = (isAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer