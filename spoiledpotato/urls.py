from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('actors/', views.actor_list, name='actor_list'),
    path('actor/<int:pk>', views.actor_detail, name='actor_detail'),
    path('movie/<int:pk>', views.movie_detail, name='movie_detail'),
    path('movie/new', views.movie_create, name='movie_create'),
]