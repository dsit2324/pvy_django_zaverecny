# Clash Royale Database

## Autor

Dominik Svoboda - třída: IT3

## Popis projektu

Webová aplikace vytvořená v Django frameworku sloužící k evidenci dat ze hry Clash Royale.

Aplikace umožňuje správu:

* hráčů
* karet
* klanů
* arén
* soubojů

## Použité technologie

* Python
* Django
* SQLite3
* Bootstrap 5
* HTML
* CSS

## Funkce aplikace

* Administrace dat pomocí Django Admin
* Výpis hráčů
* Detail hráče
* Výpis karet
* Výpis arén
* Výpis klanů
* Výpis soubojů

## Instalace

Vytvoření virtuálního prostředí:

python -m venv .venv

Aktivace prostředí:

.venv\Scripts\activate

Instalace závislostí:

pip install -r requirements.txt

Spuštění serveru:

python manage.py runserver

## Odevzdání a poznámky

- Projekt obsahuje datový model s více než 3 navzájem propojenými objekty (`Player`, `Card`, `Clan`, `Arena`, `Battle`, `PlayersCards`).
- V databázi jsou nahraná ukázková data (fixtures) — viz `fixtures/sample_data.json`.
- Pro rychlé ověření je vytvořen superuživatel: uživatel `admin`, heslo `adminpass`. Z bezpečnostních důvodů heslo po přihlášení prosím změňte.

## Jak odevzdat

1. Zkontrolujte repozitář na GitHubu (remote): https://github.com/dsit2324/pvy_django_zaverecny
2. Ujistěte se, že `requirements.txt` je v kořenovém adresáři a že `fixtures/sample_data.json` je přítomný.
3. Vygenerujte migrační soubory a spusťte migrations, pokud budete nasazovat jinde:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/sample_data.json
```

4. Přihlaste se do administrace: `http://127.0.0.1:8000/admin/` (přihlašovací údaje viz výše).

