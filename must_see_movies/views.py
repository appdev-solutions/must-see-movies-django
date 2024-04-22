from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Movie, Director

class MovieListView(ListView):
    model = Movie
    template_name = "movie_list.html"

class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie_detail.html"

class MovieCreateView(CreateView):
    model = Movie
    template_name = "movie_new.html"
    fields = ["description", "duration", "image", "title", "year", "director"]

class MovieUpdateView(UpdateView):
    model = Movie
    template_name = "movie_edit.html"
    fields = ["description", "duration", "image", "title", "year", "director"]

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = "movie_delete.html"
    success_url = reverse_lazy("movies")

class DirectorListView(ListView):
    model = Director
    template_name = "director_list.html"

class DirectorDetailView(DetailView):
    model = Director
    template_name = "director_detail.html"

class DirectorCreateView(CreateView):
    model = Director
    template_name = "director_new.html"
    fields = ["name", "bio", "dob", "image"]

class DirectorUpdateView(UpdateView):
    model = Director
    template_name = "director_edit.html"
    fields = ["name", "bio", "dob", "image"]

class DirectorDeleteView(DeleteView):
    model = Director
    template_name = "director_delete.html"
    success_url = reverse_lazy("directors")