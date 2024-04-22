from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "title",
        "year",
        "created_at",
        "updated_at",
    ]   

admin.site.register(Movie, MovieAdmin)
