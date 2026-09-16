# tracker/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from .models import TrackedSearch, Listing, PriceSnapshot
from .autodev_client import search_listings

@shared_task
def poll_tracked_searches():
    for ts in TrackedSearch.objects.filter(active=True):
        for item in search_listings(ts):
            vin = item["vehicle"]["vin"]
            price = item["retailListing"]["price"]
            listing, created = Listing.objects.get_or_create(
                vin=vin,
                defaults={
                    "tracked_search": ts,
                    "year": item["vehicle"]["year"],
                    "make": item["vehicle"]["make"],
                    "model": item["vehicle"]["model"],
                    "first_seen_price": price,
                    "current_price": price,
                    "url": item.get("retailListing", {}).get("vdpUrl", ""),
                },
            )
            if not created and price < listing.current_price:
                drop = listing.current_price - price
                listing.current_price = price
                listing.save()
                send_mail(
                    subject=f"Price drop: {listing.year} {listing.make} {listing.model}",
                    message=f"Dropped ${drop} to ${price}. {listing.url}",
                    from_email=None,
                    recipient_list=[ts.alert_email],
                )
            PriceSnapshot.objects.create(listing=listing, price=price)