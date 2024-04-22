from django.db import models

class Movie(models.Model):
    description = models.TextField()
    duration = models.IntegerField()
    image = models.CharField(max_length=255)
    title = models.CharField(max_length=255, unique=True)
    year = models.IntegerField()

    def __str__(self):
        return self.title
