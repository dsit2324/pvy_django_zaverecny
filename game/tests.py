from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Arena, Clan, Player


class PlayerProfileTests(TestCase):
    def setUp(self):
        self.arena = Arena.objects.create(
            arena_id=1,
            name='Arena Test',
            min_battles_won=0,
            max_battles_won=10,
        )
        self.clan = Clan.objects.create(
            clan_id=1,
            name='Clan Test',
            created_at=timezone.now(),
        )
        self.player = Player.objects.create(
            player_id=1,
            username='alice',
            battles_won=5,
            arena=self.arena,
            clan=self.clan,
            created_at=timezone.now(),
        )

    def test_players_page_links_to_real_player_profile(self):
        response = self.client.get(reverse('players'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'/players/{self.player.player_id}/')

    def test_player_profile_page_loads(self):
        response = self.client.get(reverse('player_detail', args=[self.player.player_id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.player.username)


class FavoritePlayersTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='favor', password='StrongPass1!')
        self.arena = Arena.objects.create(
            arena_id=10,
            name='Arena Fav',
            min_battles_won=0,
            max_battles_won=20,
        )
        self.clan = Clan.objects.create(
            clan_id=10,
            name='Clan Fav',
            created_at=timezone.now(),
        )
        self.player = Player.objects.create(
            player_id=10,
            username='favplayer',
            battles_won=2,
            arena=self.arena,
            clan=self.clan,
            created_at=timezone.now(),
        )

    def test_toggle_favorite_player_stores_player_in_session(self):
        self.client.login(username='favor', password='StrongPass1!')

        response = self.client.get(reverse('toggle_favorite_player', args=[self.player.player_id]), follow=False)

        self.assertEqual(response.status_code, 302)
        self.assertIn(self.player.player_id, self.client.session['favorite_players'])

    def test_home_page_shows_favorite_players_for_logged_in_users(self):
        self.client.login(username='favor', password='StrongPass1!')
        session = self.client.session
        session['favorite_players'] = [self.player.player_id]
        session.save()

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Oblíbení hráči')
        self.assertContains(response, self.player.username)


class RegistrationTests(TestCase):
    def test_register_user_success_redirects_to_login(self):
        response = self.client.post(
            reverse('register'),
            {
                'username': 'newuser',
                'email': 'newuser@example.com',
                'password1': 'Testovaci123!',
                'password2': 'Testovaci123!',
            },
            follow=False,
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/')

    def test_register_user_with_weak_password_shows_errors(self):
        response = self.client.post(
            reverse('register'),
            {
                'username': 'weakuser',
                'email': 'weak@example.com',
                'password1': '123456',
                'password2': '123456',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Registrace')
        self.assertContains(response, 'This password is too short')
