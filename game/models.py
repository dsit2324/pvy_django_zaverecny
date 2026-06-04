from django.db import models


class Arena(models.Model):
    arena_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    min_battles_won = models.IntegerField()
    max_battles_won = models.IntegerField()

    class Meta:
        ordering = ['min_battles_won']
        verbose_name = 'Arena'
        verbose_name_plural = 'Arenas'
        db_table = 'game_arena'


class Clan(models.Model):
    clan_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        ordering = ['name']
        verbose_name = 'Clan'
        verbose_name_plural = 'Clans'
        db_table = 'game_clan'


class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    battles_won = models.IntegerField()

    arena = models.ForeignKey(
        Arena,
        on_delete=models.CASCADE,
        db_column='arena_id'
    )

    clan = models.ForeignKey(
        Clan,
        on_delete=models.CASCADE,
        db_column='clan_id'
    )

    created_at = models.DateTimeField()

    class Meta:
        ordering = ['username']
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        db_table = 'game_player'


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

    class Meta:
        ordering = ['name']
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'
        db_table = 'game_card'


class PlayersCards(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        db_column='player_id'
    )

    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        db_column='card_id'
    )

    level = models.IntegerField()

    class Meta:
        unique_together = ('player', 'card')
        verbose_name = 'Player Card'
        verbose_name_plural = 'Player Cards'
        db_table = 'game_playerscards'


class Battle(models.Model):
    battle_id = models.IntegerField(primary_key=True)

    player1 = models.ForeignKey(
        Player,
        related_name='player1_battles',
        on_delete=models.CASCADE,
        db_column='player1_id'
    )

    player2 = models.ForeignKey(
        Player,
        related_name='player2_battles',
        on_delete=models.CASCADE,
        db_column='player2_id'
    )

    winner = models.ForeignKey(
        Player,
        related_name='won_battles',
        on_delete=models.CASCADE,
        db_column='winner_id'
    )

    played_at = models.DateTimeField()
    duration = models.IntegerField()

    class Meta:
        ordering = ['-played_at']
        verbose_name = 'Battle'
        verbose_name_plural = 'Battles'
        db_table = 'game_battle'
