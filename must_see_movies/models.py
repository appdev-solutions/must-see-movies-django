from django.db import models
from django.urls import reverse

class Director(models.Model):
    bio = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("director", kwargs={"pk": self.pk})

class Movie(models.Model):
    description = models.TextField()
    duration = models.IntegerField()
    image = models.CharField(max_length=255)
    title = models.CharField(max_length=255, unique=True)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie", kwargs={"pk": self.pk})

class Actor(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("actor", kwargs={"pk": self.pk})

class Character(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
