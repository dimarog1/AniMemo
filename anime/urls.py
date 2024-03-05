from django.urls import path
from . import views

urlpatterns = [
    path('', views.animes, name='animes'),
]
