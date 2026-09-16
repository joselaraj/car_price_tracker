from rest_framework import serializers
from .models import TrackedSearch, Listing, PriceSnapshot

class PriceSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceSnapshot
        fields = ["price", "recorded_at"]

class ListingSerializer(serializers.ModelSerializer):
    history = PriceSnapshotSerializer(many=True, read_only=True)
    tracked_search_name = serializers.CharField(source="tracked_search.name", read_only=True)

    class Meta:
        model = Listing
        fields = [
            "id", "vin", "year", "make", "model",
            "first_seen_price", "current_price", "url",
            "last_updated", "tracked_search_name", "history",
        ]

class TrackedSearchSerializer(serializers.ModelSerializer):
    listing_count = serializers.IntegerField(source="listing_set.count", read_only=True)

    class Meta:
        model = TrackedSearch
        fields = "__all__"