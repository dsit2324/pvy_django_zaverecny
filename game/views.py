from django.shortcuts import render, get_object_or_404
from .models import Player


def home(request):
    return render(request, "home.html")


def players_list(request):
    players = Player.objects.all()
    return render(request, "players.html", {"players": players})


def player_detail(request, id):
    player = get_object_or_404(Player, player_id=id)
    return render(request, "player_detail.html", {"player": player})