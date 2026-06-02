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
        db_table = 'arenas'

    def __str__(self):
        return self.name


class Clan(models.Model):
    clan_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        ordering = ['name']
        verbose_name = 'Clan'
        verbose_name_plural = 'Clans'
        db_table = 'clans'

    def __str__(self):
        return self.name


class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    battles_won = models.IntegerField()
    arena = models.ForeignKey(Arena, on_delete=models.CASCADE)
    clan = models.ForeignKey(Clan, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    class Meta:
        ordering = ['username']
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        db_table = 'players'

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

    class Meta:
        ordering = ['name']
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'
        db_table = 'cards'

    def __str__(self):
        return self.name


class PlayersCards(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    level = models.IntegerField()

    class Meta:
        unique_together = ('player', 'card')
        verbose_name = 'Player Card'
        verbose_name_plural = 'Player Cards'
        db_table = 'players_cards'

    def __str__(self):
        return f"{self.player} - {self.card} (lvl {self.level})"


class Battle(models.Model):
    battle_id = models.IntegerField(primary_key=True)
    player1 = models.ForeignKey(
        Player,
        related_name='player1_battles',
        on_delete=models.CASCADE
    )
    player2 = models.ForeignKey(
        Player,
        related_name='player2_battles',
        on_delete=models.CASCADE
    )
    winner = models.ForeignKey(
        Player,
        related_name='won_battles',
        on_delete=models.CASCADE
    )
    played_at = models.DateTimeField()
    duration = models.IntegerField()

    class Meta:
        ordering = ['-played_at']
        verbose_name = 'Battle'
        verbose_name_plural = 'Battles'
        db_table = 'battles'

    def __str__(self):
        return f"{self.player1} vs {self.player2} - Winner: {self.winner}"