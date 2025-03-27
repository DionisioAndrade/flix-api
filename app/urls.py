from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView,GenreRetrieveUpdateDestroyView
from actors.views import ActorCreateListView,ActorRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateListView.as_view(),name='genres-create-list-view'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
    path('actors/', ActorCreateListView.as_view(), name='actors-create-list-view'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
]
