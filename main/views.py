from django.shortcuts import render
from anime.models import Anime


def index(request):
    animes = Anime.objects.all()
    data = {
        'title': 'Библиотека',
        'animes': animes
    }
    return render(request, 'main/index.html', data)
