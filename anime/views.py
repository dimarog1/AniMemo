from django.shortcuts import render, redirect
from .models import AnimeModel
from django.views.generic import DetailView, DeleteView
from AnimeGoParser.animego_parser import api
from AnimeGoParser.anime_preview import AnimePreview
from django.http import HttpResponseServerError, Http404
from urllib.parse import unquote, quote


def index(request):
    animes_saved = AnimeModel.objects.filter(user_id=request.user.id)
    animes = [AnimePreview(anime_saved.english_name, anime_saved.russian_name, anime_saved.poster, anime_saved.rating,
                           anime_saved.url, quote(anime_saved.url)) for anime_saved in animes_saved]

    data = {
        'title': 'Библиотека',
        'animes': animes if animes else None
    }
    return render(request, 'anime/index.html', data)


def anime_info(request, encoded_url):
    url = unquote(encoded_url)

    # Проверяем, есть ли это аниме в базе данных
    try:
        anime_saved = AnimeModel.objects.get(url=url, user_id=request.user.id)
        source = anime_saved.source
        anime_id = anime_saved.id
        saved = anime_saved.user_id == request.user.id
    except AnimeModel.DoesNotExist:
        source = None
        anime_id = None
        saved = False

    # Если аниме не сохранено
    anime = api.get_anime(url)
    if not anime:
        return render(request, 'anime/page_not_found.html', {'title': 'Not Found'})

    data = {
        'title': anime.russian,
        'saved': saved,
        'anime_id': anime_id,
        'anime': anime,
        'source': source,
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


def add_anime(request, encoded_url):
    query_dict = request.POST
    url = unquote(encoded_url)
    try:
        source = query_dict.get('source')
        anime = api.get_anime(url)
    except Exception as e:
        print(e)
        return HttpResponseServerError

    if AnimeModel.objects.filter(url=url, user_id=request.user.id).exists():
        return redirect('home')

    if not (source.startswith('https://') or source.startswith('http://')):
        source = None
    anime = AnimeModel(user_id=request.user.id, english_name=anime.name, russian_name=anime.russian, poster=anime.poster, rating=anime.rating,
                       url=url, source=source)
    anime.save()
    return redirect('home')


class AnimeDeleteView(DeleteView):
    model = AnimeModel
    success_url = '/'
