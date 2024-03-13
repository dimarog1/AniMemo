from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search_anime', views.search_anime, name='search_anime'),
    path('anime_info/<path:encoded_url>', views.anime_info, name='anime_info'),
    path('add_anime/<path:encoded_url>', views.add_anime, name='add_anime'),
    path('delete_anime/<int:pk>', views.AnimeDeleteView.as_view(), name='delete_anime'),
]
