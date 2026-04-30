from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.players_list),
    path('cards/', views.cards_list),
]