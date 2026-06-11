from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView


from .forms import RegisterForm
from .models import Player, Card, Battle, Clan, Arena


class CustomLoginView(LoginView):
    # Poznámka pro vývojáře: vlastní login view přidává uživatelskou zprávu po úspěšném přihlášení.
    template_name = "registration/login.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Vítej zpět, {self.request.user.username}! 👋")
        return response

def register(request):
    # Poznámka pro vývojáře: registrace používá vlastní formulář a přesměrování na login po úspěchu.
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})


def home(request):
    # Poznámka pro vývojáře: homepage agreguje základní statistiky a seznam oblíbených hráčů pro přihlášené uživatele.
    favorite_ids = request.session.get('favorite_players', [])
    favorite_players = Player.objects.filter(player_id__in=favorite_ids) if favorite_ids else []

    context = {
        "players_count": Player.objects.count(),
        "cards_count": Card.objects.count(),
        "battles_count": Battle.objects.count(),
        "is_authenticated": request.user.is_authenticated,
        "favorite_players": favorite_players,
    }
    return render(request, "home.html", context)


def toggle_favorite_player(request, player_id):
    # Poznámka pro vývojáře: oblíbení hráči jsou ukládáni do session, takže fungují i bez databázové tabulky.
    if not request.user.is_authenticated:
        return redirect('login')

    favorite_players = set(request.session.get('favorite_players', []))
    if player_id in favorite_players:
        favorite_players.remove(player_id)
        messages.info(request, 'Hráč byl odebrán z oblíbených.')
    else:
        favorite_players.add(player_id)
        messages.success(request, 'Hráč byl přidán do oblíbených.')

    request.session['favorite_players'] = list(favorite_players)
    return redirect('players')


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