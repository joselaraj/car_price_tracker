from rest_framework import viewsets
from tracker.models import TrackedSearch, Listing
from tracker.serializers import TrackedSearchSerializer, ListingSerializer

class TrackedSearchViewSet(viewsets.ModelViewSet):
    queryset = TrackedSearch.objects.all()
    serializer_class = TrackedSearchSerializer

class ListingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Listing.objects.all().order_by("current_price")
    serializer_class = ListingSerializer