from rest_framework.routers import DefaultRouter

from .views import ExchangeViewSet

router = DefaultRouter()

router.register(
    "exchange",
    ExchangeViewSet,
    basename="exchange"
)

urlpatterns = router.urls