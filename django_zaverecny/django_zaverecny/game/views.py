from django.http import JsonResponse
from .models import Player, Card


def players_list(request):
    players = Player.objects.all().values()
    return JsonResponse(list(players), safe=False)


def cards_list(request):
    cards = Card.objects.all().values()
    return JsonResponse(list(cards), safe=False)