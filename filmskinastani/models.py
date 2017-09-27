from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Festival(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    #location
    user = models.ForeignKey(User)
    movies = models.ManyToManyField("Movie")
    awards = models.ManyToManyField("Award")

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    length = models.IntegerField()
    votes = models.IntegerField(default=0)
    actors = models.ManyToManyField("Actor")
    producent = models.ForeignKey("Producent")


    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    votes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

#do tuka gi vklucuva templejtot

class Actor(models.Model):
    full_name = models.CharField(max_length=100)
    num_oscars = models.IntegerField(default=0)
    num_gramys = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    award = models.ForeignKey("Award", null=True, blank=True)

    def __str__(self):
        return self.full_name


# nagradite mozat da bidat: The Academy award(aka Oscars), Golden Globe, The Emmy, MTV movie awards, The People's choice awards,
# Hollywood Film awards, Teen choice awards...
class Award(models.Model):
    name_of_award = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_award


class Producent(models.Model):
    full_name = models.CharField(max_length=100)
    number_films = models.IntegerField(default=0)
    number_awards = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    award = models.ForeignKey(Award, null=True, blank=True)

    def __str__(self):
        return self.full_name
