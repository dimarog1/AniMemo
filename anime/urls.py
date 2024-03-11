from django.urls import path
from . import views
from AnimeGoParser.anime_preview import AnimePreview

urlpatterns = [
    path('', views.index, name='home'),
    path('search_anime', views.search_anime, name='search_anime'),
    # path('<int:pk>', views.AnimeDetailView.as_view(), name='anime_info'),
    path('anime_info/<path:encoded_url>', views.anime_info, name='anime_info'),
]
