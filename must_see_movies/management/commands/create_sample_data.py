from django.core.management.base import BaseCommand
from django.core.management import call_command
from faker import Faker

from must_see_movies.models import Director, Movie, Actor, Character

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command("flush", "--noinput") # Flush database, equivalent to "python manage.py flush"

        fake = Faker()
        Faker.seed(1) # generate consistent smaple data

        for i in range(50):
            Director.objects.create(name=fake.name(), bio=fake.sentence(nb_words=20))
            Movie.objects.create(
                title=fake.text(max_nb_chars=100),
                description=fake.sentence(nb_words=20), 
                duration=fake.random_int(min=80, max=220),
                year=fake.random_int(min=1950, max=2020),
                director=Director.objects.order_by("?").first()
            )
            Actor.objects.create(name=fake.name())
            Character.objects.create(name=fake.name(), actor=Actor.objects.order_by("?").first(), movie=Movie.objects.order_by("?").first())

        self.stdout.write(self.style.SUCCESS("Data created successfully"))