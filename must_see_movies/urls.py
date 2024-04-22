from django.urls import path
from .views import (
    MovieListView,
    MovieDetailView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
)

urlpatterns = [
    path("movies/", MovieListView.as_view(), name="movies"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movie"),
    path("movies/new/", MovieCreateView.as_view(), name="movie_create"),
    path("movies/<int:pk>/update/", MovieUpdateView.as_view(), name="movie_update"),
    path("movies/<int:pk>/delete/", MovieDeleteView.as_view(), name="movie_delete"),
]