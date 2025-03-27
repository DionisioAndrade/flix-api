from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView,GenreRetrieveUpdateDestroyView
from actors.views import ActorCreateListView,ActorRetrieveUpdateDestroyView
from movies.views import MovieCreateListView,MovieRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/', GenreCreateListView.as_view(),name='genres-create-list-view'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
    
    path('actors/', ActorCreateListView.as_view(), name='actors-create-list-view'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
    
    path('movies/', MovieCreateListView.as_view(), name='movies-create-list-view'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail-view'),
]
