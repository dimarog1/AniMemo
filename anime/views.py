from django.shortcuts import render, redirect
from .models import Anime


def animes(request):
    all_animes = Anime.objects.all()
    data = {
        'animes': all_animes
    }
    return redirect('home')
