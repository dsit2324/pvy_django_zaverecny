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
- `django_zaverecny/` – hlavní Django project settings

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
4. Pokud chcete použít MySQL, nastavte proměnné prostředí před migrací
   ```bash
   export MYSQL_DATABASE=django_zaverecny
   export MYSQL_USER=root
   export MYSQL_PASSWORD=secret
   export MYSQL_HOST=127.0.0.1
   export MYSQL_PORT=3306
   ```
5. Spusťte migrace a vytvořte demo data
   ```bash
   python manage.py migrate
   ```
6. Spusťte aplikaci
   ```bash
   python manage.py runserver
   ```

> Pokud není `MYSQL_DATABASE` nastaveno, aplikace použije lokální SQLite databázi `db.sqlite3`.

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

