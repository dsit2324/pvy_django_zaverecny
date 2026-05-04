from django.shortcuts import render, get_object_or_404
from .models import Player, Card, Battle, Clan, Arena


def home(request):
    return render(request, "home.html")


def players_list(request):
    players = Player.objects.all()
    return render(request, "players.html", {"players": players})


def player_detail(request, id):
    player = get_object_or_404(Player, player_id=id)
    return render(request, "player_detail.html", {"player": player})


def cards_list(request):
    cards = Card.objects.all()
    return render(request, "cards.html", {"cards": cards})


def battles_list(request):
    battles = Battle.objects.all()
    return render(request, "battles.html", {"battles": battles})


def clans_list(request):
    clans = Clan.objects.all()
    return render(request, "clans.html", {"clans": clans})


def arenas_list(request):
    arenas = Arena.objects.all()
    return render(request, "arenas.html", {"arenas": arenas})