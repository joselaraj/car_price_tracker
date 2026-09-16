from django.contrib import admin
from .models import TrackedSearch, Listing, PriceSnapshot

admin.site.register(TrackedSearch)
admin.site.register(Listing)
admin.site.register(PriceSnapshot)