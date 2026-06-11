from datetime import datetime, timezone

from django.db import migrations


def create_initial_data(apps, schema_editor):
    Arena = apps.get_model('game', 'Arena')
    Clan = apps.get_model('game', 'Clan')
    Player = apps.get_model('game', 'Player')
    Card = apps.get_model('game', 'Card')
    PlayersCards = apps.get_model('game', 'PlayersCards')
    Battle = apps.get_model('game', 'Battle')

    arena1 = Arena.objects.create(
        arena_id=1,
        name='Training Camp',
        min_battles_won=0,
        max_battles_won=9,
    )
    arena2 = Arena.objects.create(
        arena_id=2,
        name='Goblin Stadium',
        min_battles_won=10,
        max_battles_won=99,
    )

    clan1 = Clan.objects.create(
        clan_id=1,
        name='Alpha Squad',
        created_at=datetime(2026, 1, 10, 10, 0, tzinfo=timezone.utc),
    )
    clan2 = Clan.objects.create(
        clan_id=2,
        name='Bravo Club',
        created_at=datetime(2026, 2, 20, 12, 0, tzinfo=timezone.utc),
    )

    player1 = Player.objects.create(
        player_id=1,
        username='alice',
        battles_won=5,
        arena=arena1,
        clan=clan1,
        created_at=datetime(2026, 3, 1, 9, 0, tzinfo=timezone.utc),
    )
    player2 = Player.objects.create(
        player_id=2,
        username='bob',
        battles_won=8,
        arena=arena2,
        clan=clan2,
        created_at=datetime(2026, 3, 2, 11, 0, tzinfo=timezone.utc),
    )

    card1 = Card.objects.create(
        card_id=1,
        name='Fireball',
        description='Deals area damage',
        rarity='rare',
        elixircost=4,
        type='spell',
    )
    card2 = Card.objects.create(
        card_id=2,
        name='Knight',
        description='Melee troop',
        rarity='common',
        elixircost=3,
        type='troop',
    )

    PlayersCards.objects.create(
        player=player1,
        card=card1,
        level=4,
    )
    PlayersCards.objects.create(
        player=player2,
        card=card2,
        level=2,
    )

    Battle.objects.create(
        battle_id=1,
        player1=player1,
        player2=player2,
        winner=player2,
        played_at=datetime(2026, 5, 1, 15, 30, tzinfo=timezone.utc),
        duration=180,
    )


def remove_initial_data(apps, schema_editor):
    Battle = apps.get_model('game', 'Battle')
    PlayersCards = apps.get_model('game', 'PlayersCards')
    Player = apps.get_model('game', 'Player')
    Card = apps.get_model('game', 'Card')
    Clan = apps.get_model('game', 'Clan')
    Arena = apps.get_model('game', 'Arena')

    Battle.objects.filter(battle_id=1).delete()
    PlayersCards.objects.filter(card__card_id__in=[1, 2], player__player_id__in=[1, 2]).delete()
    Player.objects.filter(player_id__in=[1, 2]).delete()
    Card.objects.filter(card_id__in=[1, 2]).delete()
    Clan.objects.filter(clan_id__in=[1, 2]).delete()
    Arena.objects.filter(arena_id__in=[1, 2]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data, remove_initial_data),
    ]
