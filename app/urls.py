from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView,GenreRetrieveUpdateDestroyView
from actors.views import ActorCreateListView,ActorRetrieveUpdateDestroyView
from movies.views import MovieCreateListView,MovieRetrieveUpdateDestroyView
from reviews.views import ReviewListCreateView,ReviewRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/', GenreCreateListView.as_view(),name='genres-create-list-view'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
    
    path('actors/', ActorCreateListView.as_view(), name='actors-create-list-view'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
    
    path('movies/', MovieCreateListView.as_view(), name='movies-create-list-view'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail-view'),
    
    path('reviews/', ReviewListCreateView.as_view(), name='reviews-create-list-view'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-view'),
]
