from django.shortcuts import render , redirect
from .models import Movie, Actor
from .forms import MovieForm, ActorForm, SearchForm

def home_page(request):
    recent_movies = Movie.objects.order_by('-id')[:5]
    return render(request, 'spoiledpotato/home_page.html', {'recent_movies': recent_movies})

def actor_list(request):
    actors = Actor.objects.all()
    return render(request, 'spoiledpotato/actor_list.html',{'actors':actors})

def actor_create(request):
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            actor = form.save()
            return redirect('actor_detail', pk=actor.pk)
    else:
        form = ActorForm()
    return render(request, 'spoiledpotato/actor_form.html', {'form': form}) 

def actor_detail(request, pk):
    actor = Actor.objects.get(id=pk)
    return render(request, 'spoiledpotato/actor_detail.html', {'actor': actor})

def actor_delete(request, pk):
    Actor.objects.get(id=pk).delete()
    return redirect('actor_list')

def actor_edit(request, pk):
    actor = Actor.objects.get(id=pk)
    if request.method == "POST":
        form = Actor.objects.get(request.POST, instance=actor)
        if form.is_valid():
            actor = form.save()
            return redirect('actor_detail', pk=actor.pk)
    else:
        form = ActorForm(instance=actor)
    return render(request, 'spoiledpotato/actor_form.html', {'form': form})

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'spoiledpotato/movie_list.html', {'movies': movies})

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'spoiledpotato/movie_form.html', {'form': form})

def movie_detail(request, pk):
    movie = Movie.objects.get(id=pk)
    return render(request, 'spoiledpotato/movie_detail.html', {'movie': movie})

def movie_delete(request, pk):
    Movie.objects.get(id=pk).delete()
    return redirect('movie_list')

def movie_edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'spoiledpotato/movie_form.html', {'form': form})

def search_view(request):
    form = SearchForm()
    results = None

    if request.method == 'GET' and 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = {
                'movies': Movie.objects.filter(title__icontains=query),
                'actors': Actor.objects.filter(name__icontains=query)
            }

    return render(request, 'spoiledpotato/search_results.html', {'form': form, 'results': results})
# Create your views here.
