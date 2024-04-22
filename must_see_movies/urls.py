from django.urls import path
from .views import (
    MovieListView,
    MovieDetailView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
    DirectorListView,
    DirectorDetailView,
    DirectorCreateView,
    DirectorUpdateView,
    DirectorDeleteView,
)

urlpatterns = [
    path("movies/", MovieListView.as_view(), name="movies"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movie"),
    path("movies/new/", MovieCreateView.as_view(), name="movie_create"),
    path("movies/<int:pk>/update/", MovieUpdateView.as_view(), name="movie_update"),
    path("movies/<int:pk>/delete/", MovieDeleteView.as_view(), name="movie_delete"),
    path("directors/", DirectorListView.as_view(), name="directors"),
    path("directors/<int:pk>/", DirectorDetailView.as_view(), name="director"),
    path("directors/new/", DirectorCreateView.as_view(), name="director_create"),
    path("directors/<int:pk>/update/", DirectorUpdateView.as_view(), name="director_update"),
    path("directors/<int:pk>/delete/", DirectorDeleteView.as_view(), name="director_delete"),
]