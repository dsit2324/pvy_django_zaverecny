from django.urls import path
from django.contrib.auth.views import LogoutView  # <-- PŘIDÁNO
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.home),
    path('players/', views.players_list),
    path('players/<int:id>/', views.player_detail),
    path('cards/', views.cards_list),
    path('battles/', views.battles_list),
    path('clans/', views.clans_list),
    path('arenas/', views.arenas_list),
    path("register/", views.register),
    path("accounts/login/", CustomLoginView.as_view()),
    path("logout/", LogoutView.as_view(), name="logout"),  # <-- PŘIDÁNO
]