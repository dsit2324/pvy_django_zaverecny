from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('players/', views.players_list),
    path('players/<int:id>/', views.player_detail),

    path('cards/', views.cards_list),
    path('battles/', views.battles_list),
    path('clans/', views.clans_list),
    path('arenas/', views.arenas_list),
]