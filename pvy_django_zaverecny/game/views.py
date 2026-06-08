from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView

from .models import Player, Card, Battle, Clan, Arena
from .forms import RegisterForm


class CustomLoginView(LoginView):
    template_name = "registration/login.html"


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = RegisterForm()

    return render(
        request,
        "registration/register.html",
        {"form": form}
    )


def home(request):
    context = {
        "players_count": Player.objects.count(),
        "cards_count": Card.objects.count(),
        "battles_count": Battle.objects.count(),
        "clans_count": Clan.objects.count(),
        "arenas_count": Arena.objects.count(),
    }

    return render(request, "home.html", context)


def players_list(request):
    players = Player.objects.all()

    return render(
        request,
        "players.html",
        {"players": players}
    )


def player_detail(request, id):
    player = get_object_or_404(Player, player_id=id)

    return render(
        request,
        "player_detail.html",
        {"player": player}
    )


def cards_list(request):
    cards = Card.objects.all()

    return render(
        request,
        "cards.html",
        {"cards": cards}
    )


def battles_list(request):
    battles = Battle.objects.all()

    return render(
        request,
        "battles.html",
        {"battles": battles}
    )


def clans_list(request):
    clans = Clan.objects.all()

    return render(
        request,
        "clans.html",
        {"clans": clans}
    )


def arenas_list(request):
    arenas = Arena.objects.all()

    return render(
        request,
        "arenas.html",
        {"arenas": arenas}
    )