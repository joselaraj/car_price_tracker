# Car Price Tracker

A backend service that tracks used-car listings against saved search criteria and alerts you by email when a tracked vehicle's price drops.

## Why this exists

Most used-car marketplaces (Cars.com, CarGurus) explicitly prohibit automated scraping in their Terms of Service. Rather than build a scraper that violates those terms, this project uses [Auto.dev](https://auto.dev), a legitimate third-party API that aggregates dealer listing data — same end result, no legal/ethical gray area.

## Architecture

```
Django (models, admin)
      │
      ▼
Celery Beat (schedules polling every 4 hours)
      │
      ▼
Celery Worker ──► autodev_client.py ──► Auto.dev API
      │
      ▼
Diff against stored price (PriceSnapshot history)
      │
      ▼
Email alert on price drop
```

- **Django** — models (`TrackedSearch`, `Listing`, `PriceSnapshot`) and admin UI for managing tracked searches
- **Celery + Redis** — scheduled background polling, decoupled from the web process
- **Auto.dev API** — vehicle listing data (make, model, year, price, VIN, dealer URL)
- **Email alerts** — fires when a tracked listing's price drops since the last poll

## Setup

```bash
git clone <https://github.com/joselaraj/car_price_tracker.git>
cd car_price_tracker
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create `KEY.env` in the project root:
```
AUTO_DEV_API_KEY=your_key_here
```

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

In separate terminals, with Redis running:
```bash
celery -A cartracker worker --loglevel=info
celery -A cartracker beat --loglevel=info
```

## Usage

1. Log into `/admin`
2. Add a `TrackedSearch` (make, model, year range, max price, ZIP, alert email)
3. The Celery beat scheduler polls Auto.dev every 4 hours and emails you when a matching listing's price drops

## Tech stack

Python, Django, Celery, Redis, Auto.dev API, PostgreSQL/SQLite

