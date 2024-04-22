from django.contrib import admin
from .models import Movie, Director

class MovieAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "title",
        "year",
        "created_at",
        "updated_at",
    ]   

class DirectorAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "name",
        "created_at",
        "updated_at",
    ]   

admin.site.register(Movie, MovieAdmin)
admin.site.register(Director, DirectorAdmin)
