from rest_framework.routers import DefaultRouter
from .views import TrackedSearchViewSet, ListingViewSet

router = DefaultRouter()
router.register("tracked-searches", TrackedSearchViewSet)
router.register("listings", ListingViewSet)

urlpatterns = router.urls