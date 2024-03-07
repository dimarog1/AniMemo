from django.shortcuts import render, redirect
from .models import Anime, AnimePreview
from django.views.generic import DetailView
from .forms import AnimePreviewForm
from .AnimeGoParser.animego_parser import api
from django.http import HttpResponseServerError


def animes(request):
    all_animes = Anime.objects.all()
    data = {
        'animes': all_animes
    }
    return redirect('home')


class AnimeDetailView(DetailView):
    model = Anime
    template_name = 'anime/anime_info.html'
    context_object_name = 'anime'


def search_anime(request):
    query_dict = request.GET
    try:
        query = query_dict.get('q')
    except Exception as e:
        print(e)
        return HttpResponseServerError
    print(query)
    animes = api.search_anime(query)
    data = {
        'animes': animes
    }
    return render(request, 'anime/search_anime.html', data)
