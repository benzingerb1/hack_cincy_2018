from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('metronome/', views.metronome, name='metronome-app')
]