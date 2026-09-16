# tracker/autodev_client.py
import requests
from django.conf import settings

BASE_URL = "https://api.auto.dev/listings"

def search_listings(tracked_search):
    params = {
        "vehicle.make": tracked_search.make,
        "zip": tracked_search.zip_code,
        "distance": tracked_search.distance,
        "limit": 20,  # free plan cap
    }
    if tracked_search.model:
        params["vehicle.model"] = tracked_search.model
    if tracked_search.year_min or tracked_search.year_max:
        lo = tracked_search.year_min or 1900
        hi = tracked_search.year_max or 2100
        params["vehicle.year"] = f"{lo}-{hi}"
    if tracked_search.price_max:
        params["retailListing.price"] = f"1-{tracked_search.price_max}"

    resp = requests.get(
        BASE_URL,
        params=params,
        headers={"Authorization": f"Bearer {settings.AUTO_DEV_API_KEY}"},
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()["data"]