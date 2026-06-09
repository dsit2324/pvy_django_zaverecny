from django.shortcuts import render, get_object_or_404, redirect
from .models import Player, Card, Battle, Clan, Arena
from .forms import RegisterForm
from django.contrib.auth.views import LoginView

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

    return render(request, "registration/register.html", {"form": form})


def home(request):
    context = {
        "players_count": Player.objects.count(),
        "cards_count": Card.objects.count(),
        "battles_count": Battle.objects.count(),
    }
    return render(request, "home.html", context)


def players_list(request):
    return render(request, "players.html", {"players": Player.objects.all()})


def player_detail(request, id):
    player = get_object_or_404(Player, player_id=id)
    return render(request, "players_detail.html", {"player": player})


def cards_list(request):
    return render(request, "cards.html", {"cards": Card.objects.all()})


def battles_list(request):
    return render(request, "battles.html", {"battles": Battle.objects.all()})


def clans_list(request):
    return render(request, "clans.html", {"clans": Clan.objects.all()})


def arenas_list(request):
    return render(request, "arenas.html", {"arenas": Arena.objects.all()})