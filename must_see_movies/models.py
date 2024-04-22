from django.db import models
from django.urls import reverse

class Movie(models.Model):
    description = models.TextField()
    duration = models.IntegerField()
    image = models.CharField(max_length=255)
    title = models.CharField(max_length=255, unique=True)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie", kwargs={"pk": self.pk})
