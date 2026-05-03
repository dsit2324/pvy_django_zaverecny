from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('players/', views.players_list),
    path('players/<int:id>/', views.player_detail),
]