from django.urls import path
from . import views

urlpatterns = [
    path('', views.animes, name='animes'),
    path('<int:pk>', views.AnimeDetailView.as_view(), name='anime_info'),
]
