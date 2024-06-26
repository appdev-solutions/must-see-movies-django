from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Movie, Director, Actor
from .forms import CharacterForm

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

class ActorListView(ListView):
    model = Actor
    template_name = "actor_list.html"

class ActorDetailView(DetailView):
    model = Actor
    template_name = "actor_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CharacterForm()  # add form to context
        return context

    def post(self, request, *args, **kwargs):
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.actor = self.get_object()  # set actor to current actor
            character.save()
            return redirect("actor", pk=self.get_object().pk)  # redirect back to actor detail view

class ActorCreateView(CreateView):
    model = Actor
    template_name = "actor_new.html"
    fields = ["name"]

class ActorUpdateView(UpdateView):
    model = Actor
    template_name = "actor_edit.html"
    fields = ["name"]

class ActorDeleteView(DeleteView):
    model = Actor
    template_name = "actor_delete.html"
    success_url = reverse_lazy("actors")