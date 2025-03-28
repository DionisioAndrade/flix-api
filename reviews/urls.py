from django.urls import path
from . import views


urlpatterns = [

    path('reviews/', views.ReviewListCreateView.as_view(), name='reviews-create-list-view'),
    path('reviews/<int:pk>/', views.ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-view'),

]
