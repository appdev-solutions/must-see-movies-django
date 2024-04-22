from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Movie

class MovieListView(ListView):
    model = Movie
    template_name = "movie_list.html"

class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie_detail.html"

class MovieCreateView(CreateView):
    model = Movie
    template_name = "movie_new.html"
    fields = ["description", "duration", "image", "title", "year"]

class MovieUpdateView(UpdateView):
    model = Movie
    template_name = "movie_edit.html"
    fields = ["description", "duration", "image", "title", "year"]

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = "movie_delete.html"
    success_url = reverse_lazy("movies")