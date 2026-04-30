from django.http import JsonResponse
from .models import Player, Card, Battle


def players(request):
    data = list(Player.objects.values())
    return JsonResponse(data, safe=False)


def cards(request):
    data = list(Card.objects.values())
    return JsonResponse(data, safe=False)


def battles(request):
    data = list(Battle.objects.values())
    return JsonResponse(data, safe=False)