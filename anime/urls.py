from django.urls import path
from . import views

urlpatterns = [
    path('', views.animes, name='animes'),
    path('search_anime.html', views.search_anime, name='add_anime'),
    path('<int:pk>', views.AnimeDetailView.as_view(), name='anime_info'),
]
