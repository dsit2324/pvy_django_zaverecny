from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator


class Arena(models.Model):
    arena_id = models.IntegerField(primary_key=True)
    name = models.CharField(
        max_length=255,
        verbose_name="Název arény"
    )
    min_battles_won = models.IntegerField(
        verbose_name="Minimální počet výher"
    )
    max_battles_won = models.IntegerField(
        verbose_name="Maximální počet výher"
    )

    class Meta:
        verbose_name = "Aréna"
        verbose_name_plural = "Arény"
        ordering = ["min_battles_won"]
        db_table = "game_arena"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("arena_detail", args=[self.arena_id])


class Clan(models.Model):
    clan_id = models.IntegerField(primary_key=True)
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Název klanu"
    )
    created_at = models.DateTimeField(
        verbose_name="Datum vytvoření"
    )

    class Meta:
        verbose_name = "Klan"
        verbose_name_plural = "Klany"
        ordering = ["name"]
        db_table = "game_clan"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("clan_detail", args=[self.clan_id])


class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)

    username = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Uživatelské jméno"
    )

    battles_won = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="Počet výher"
    )

    arena = models.ForeignKey(
        Arena,
        on_delete=models.CASCADE,
        verbose_name="Aréna"
    )

    clan = models.ForeignKey(
        Clan,
        on_delete=models.CASCADE,
        verbose_name="Klan"
    )

    created_at = models.DateTimeField(
        verbose_name="Datum vytvoření"
    )

    class Meta:
        verbose_name = "Hráč"
        verbose_name_plural = "Hráči"
        ordering = ["username"]
        db_table = "game_player"

    def __str__(self):
        return f"{self.username} ({self.battles_won} výher)"

    def get_absolute_url(self):
        return reverse("player_detail", args=[self.player_id])


class Card(models.Model):

    RARITY_CHOICES = (
        ("common", "Common"),
        ("rare", "Rare"),
        ("epic", "Epic"),
        ("legendary", "Legendary"),
    )

    TYPE_CHOICES = (
        ("troop", "Troop"),
        ("spell", "Spell"),
        ("building", "Building"),
    )

    card_id = models.IntegerField(primary_key=True)

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Název karty"
    )

    description = models.TextField(
        verbose_name="Popis"
    )

    rarity = models.CharField(
        max_length=10,
        choices=RARITY_CHOICES,
        verbose_name="Vzácnost"
    )

    elixircost = models.IntegerField(
        validators=[MinValueValidator(0)],
        verbose_name="Cena elixíru"
    )

    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        verbose_name="Typ karty"
    )

    class Meta:
        verbose_name = "Karta"
        verbose_name_plural = "Karty"
        ordering = ["name"]
        db_table = "game_card"

    def __str__(self):
        return f"{self.name} ({self.rarity})"

    def get_absolute_url(self):
        return reverse("card_detail", args=[self.card_id])


class PlayersCards(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        verbose_name="Hráč"
    )

    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        verbose_name="Karta"
    )

    level = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name="Úroveň"
    )

    class Meta:
        verbose_name = "Karta hráče"
        verbose_name_plural = "Karty hráčů"
        unique_together = ("player", "card")
        db_table = "game_playerscards"

    def __str__(self):
        return f"{self.player.username} - {self.card.name} (lvl {self.level})"


class Battle(models.Model):
    battle_id = models.IntegerField(primary_key=True)

    player1 = models.ForeignKey(
        Player,
        related_name="player1_battles",
        on_delete=models.CASCADE,
        verbose_name="Hráč 1"
    )

    player2 = models.ForeignKey(
        Player,
        related_name="player2_battles",
        on_delete=models.CASCADE,
        verbose_name="Hráč 2"
    )

    winner = models.ForeignKey(
        Player,
        related_name="won_battles",
        on_delete=models.CASCADE,
        verbose_name="Vítěz"
    )

    played_at = models.DateTimeField(
        verbose_name="Datum souboje"
    )

    duration = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Délka souboje (s)"
    )

    class Meta:
        verbose_name = "Souboj"
        verbose_name_plural = "Souboje"
        ordering = ["-played_at"]
        db_table = "game_battle"

    def __str__(self):
        return f"{self.player1} vs {self.player2}"

    def get_absolute_url(self):
        return reverse("battle_detail", args=[self.battle_id])
