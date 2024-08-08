from django.shortcuts import render , redirect
from .models import Movie, Actor
from .forms import MovieForm

def actor_list(request):
    actors = Actor.objects.all()
    return render(request, 'spoiledpotato/actor_list.html',{'actors':actors})

def actor_detail(request, pk):
    actor = Actor.objects.get(id=pk)
    return render(request, 'spoiledpotato/actor_detail.html', {'actor': actor})

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'spoiledpotato/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = Movie.objects.get(id=pk)
    return render(request, 'spoiledpotato/movie_detail.html', {'movie': movie})

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'spoiledpotato/movie_form.html', {'form': form})


# Create your views here.
