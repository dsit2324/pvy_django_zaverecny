from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),

    path('players/', views.players_list, name='players'),
    path('players/<int:id>/', views.player_detail, name='player_detail'),

    path('cards/', views.cards_list, name='cards'),
    path('battles/', views.battles_list, name='battles'),
    path('clans/', views.clans_list, name='clans'),
    path('arenas/', views.arenas_list, name='arenas'),

    path('register/', views.register, name='register'),

    path('accounts/login/', CustomLoginView.as_view(), name='login'),

    path(
        'accounts/logout/',
        LogoutView.as_view(next_page='/'),
        name='logout'
    ),
]