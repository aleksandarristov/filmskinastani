from django.contrib.auth.models import User
from .models import Movie
from .models import Actor
from .models import Award
from .models import Producent
from .models import Festival
from .models import Comment
from .forms import MovieForm
from .forms import ActorForm
from .forms import AwardForm
from .forms import ProducentForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, RegisterForm

def index(request):
    movies = Movie.objects.all()
    festivals = Festival.objects.all()
    context = {
        "movies" : movies,
        'festivals' : festivals,
    }
    return render(request, template_name='index.html', context=context)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            u = User.objects.create_user(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'],
                                     email=form.cleaned_data['email'],
                                     first_name=form.cleaned_data['first_name'],
                                     last_name=form.cleaned_data['last_name'])
            return HttpResponseRedirect('/login')
    form = RegisterForm()
    return render(request, 'register.html', context={'form': form})

    return render(request, "register.html", {})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                return HttpResponseRedirect("/")
        else:
            return render(request, template_name='register.html')
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    form = UserLoginForm()
    return render(request, template_name='login.html', context={'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def about_view(request):
    return render(request, template_name='about.html')

def forum_view(request):
    return render(request, template_name='forum.html')

'''def movie_details(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    context = { 'movie': movie }
    return render(request, template_name='index.html', context = context)
'''

def movie_view(request):
    return render(request, template_name='')

def movie_form_view(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            movie.save()
            return HttpResponseRedirect('/')
    form = MovieForm()
    return render(request, 'movie_form.html', {'form': form})

def movie_actor_view(request):
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            actor = form.save()
            actor.save()
            return HttpResponseRedirect('/')
    form = ActorForm()
    return render(request, 'actor_form.html', {'form': form})

def movie_award_view(request):
    if request.method == 'POST':
        form = AwardForm(request.POST)
        if form.is_valid():
            award = form.save()
            award.save()
            return HttpResponseRedirect('/')
    form = AwardForm()
    return render(request, 'award_form.html', {'form': form})

def movie_producent_view(request):
    if request.method == 'POST':
        form = ProducentForm(request.POST)
        if form.is_valid():
            producent = form.save()
            producent.save()
            return HttpResponseRedirect('/')
    form = ProducentForm()
    return render(request, 'producent_form.html', {'form': form})

def profile_view(request):
    return render(request, template_name='profile.html')