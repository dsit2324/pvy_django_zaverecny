from django.db import models


class Arena(models.Model):
    arena_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    min_battles_won = models.IntegerField()
    max_battles_won = models.IntegerField()

    def __str__(self):
        return self.name


class Clan(models.Model):
    clan_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    battles_won = models.IntegerField()
    arena = models.ForeignKey(Arena, on_delete=models.CASCADE)
    clan = models.ForeignKey(Clan, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.username


class Card(models.Model):

    RARITY_CHOICES = [
        ("common", "Common"),
        ("rare", "Rare"),
        ("epic", "Epic"),
        ("legendary", "Legendary"),
    ]

    TYPE_CHOICES = [
        ("troop", "Troop"),
        ("spell", "Spell"),
        ("building", "Building"),
    ]

    card_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    rarity = models.CharField(max_length=10, choices=RARITY_CHOICES)
    elixircost = models.IntegerField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name


class PlayersCards(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    level = models.IntegerField()

    class Meta:
        unique_together = ("player", "card")


class Battle(models.Model):
    battle_id = models.IntegerField(primary_key=True)
    player1 = models.ForeignKey(Player, related_name="player1", on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name="player2", on_delete=models.CASCADE)
    winner = models.ForeignKey(Player, related_name="winner", on_delete=models.CASCADE)
    played_at = models.DateTimeField()
    duration = models.IntegerField()