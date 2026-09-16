# tracker/models.py
from django.db import models

class TrackedSearch(models.Model):
    name = models.CharField(max_length=100)          # "2020-2023 Civic, Chicago"
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50, blank=True)
    year_min = models.IntegerField(null=True, blank=True)
    year_max = models.IntegerField(null=True, blank=True)
    price_max = models.IntegerField(null=True, blank=True)
    zip_code = models.CharField(max_length=10)
    distance = models.IntegerField(default=50)
    alert_email = models.EmailField()
    active = models.BooleanField(default=True)

class Listing(models.Model):
    vin = models.CharField(max_length=17, unique=True)
    tracked_search = models.ForeignKey(TrackedSearch, on_delete=models.CASCADE)
    year = models.IntegerField()
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    first_seen_price = models.IntegerField()
    current_price = models.IntegerField()
    url = models.URLField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)

class PriceSnapshot(models.Model):
    listing = models.ForeignKey(Listing, related_name="history", on_delete=models.CASCADE)
    price = models.IntegerField()
    recorded_at = models.DateTimeField(auto_now_add=True)