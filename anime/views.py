from django.shortcuts import render, redirect
from .models import Anime
from django.views.generic import DetailView


def animes(request):
    all_animes = Anime.objects.all()
    data = {
        'animes': all_animes
    }
    return redirect('home')


def add_anime(request):
    pass


class AnimeDetailView(DetailView):
    model = Anime
    template_name = 'anime/anime_info.html'
    context_object_name = 'anime'
