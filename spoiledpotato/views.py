from django.shortcuts import render
from .models import Movie, Actor

def actor_list(request):
    actors = Actor.objects.all()
    return render(request, 'spoiledpotato/actor_list.html',{'actors':actors})

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'spoiledpotato/movie_list.html', {'movies': movies})

# Create your views here.
