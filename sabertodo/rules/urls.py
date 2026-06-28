from rest_framework.routers import DefaultRouter
from .views import RuleViewSet

router = DefaultRouter()

router.register(r"rule", RuleViewSet, basename="rule")

urlpatterns = router.urls