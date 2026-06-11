# Clash Royale Database

Django aplikace pro přehled hráčů, karet, klanů, arén a soubojů z hry Clash Royale.

## Co aplikace umí

- prohlížení seznamu hráčů a detailů profilu
- přehled karet, klanů, arén a soubojů
- registrace a přihlášení uživatelů
- osobní funkce pro přihlášené uživatele, například ukládání oblíbených hráčů
- administrace dat přes Django Admin

## Technologie

- Python 3
- Django
- SQLite
- Bootstrap 5
- HTML / CSS

## Struktura projektu

- `game/` – modely, formuláře, view, URL a testy
- `templates/` – šablony pro rozhraní aplikace
- `fixtures/` – ukázková data pro naplnění databáze

## Instalace

1. Vytvořte virtuální prostředí
   ```bash
   python -m venv .venv
   ```
2. Aktivujte prostředí
   ```bash
   .venv\Scripts\activate
   ```
   nebo na Linux/macOS:
   ```bash
   source .venv/bin/activate
   ```
3. Nainstalujte závislosti
   ```bash
   pip install -r requirements.txt
   ```
4. Spusťte migrace a načtěte demo data
   ```bash
   python manage.py migrate
   python manage.py loaddata fixtures/sample_data.json
   ```
5. Spusťte aplikaci
   ```bash
   python manage.py runserver
   ```

## Přístupové údaje

- webová aplikace: http://127.0.0.1:8000/
- administrace: http://127.0.0.1:8000/admin/
- výchozí testovací účet pro admin: `admin / adminpass`

## Testování

Pro ověření funkčnosti projektu spusťte:

```bash
python manage.py test
```

## Poznámky

Projekt obsahuje modely `Player`, `Card`, `Clan`, `Arena`, `Battle` a `PlayersCards` a je připravený pro další rozšíření o další funkce pro přihlášené uživatele.

