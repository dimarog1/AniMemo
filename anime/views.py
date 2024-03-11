from django.shortcuts import render, redirect
from .models import Anime
from django.views.generic import DetailView
from AnimeGoParser.animego_parser import api
from django.http import HttpResponseServerError, Http404
from urllib.parse import unquote


def index(request):
    animes = Anime.objects.all()
    data = {
        'title': 'Библиотека',
        'animes': animes
    }
    return render(request, 'anime/index.html', data)


class AnimeDetailView(DetailView):
    model = Anime
    template_name = 'anime/anime_info.html'
    context_object_name = 'anime'


def anime_info(request, encoded_url):
    anime = api.get_anime(unquote(encoded_url))
    if not anime:
        return render(request, 'anime/page_not_found.html', {'title': 'Not Found'})
    data = {
        'title': anime.russian,
        'anime': anime
    }
    return render(request, 'anime/anime_info.html', data)


def search_anime(request):
    query_dict = request.GET
    try:
        query = query_dict.get('q')
    except Exception as e:
        print(e)
        return HttpResponseServerError
    animes = api.search_anime_preview(query)
    data = {
        'animes': animes,
        'query': query
    }
    return render(request, 'anime/search_anime.html', data)
