from rest_framework.routers import DefaultRouter
from .views import BrandViewSet, CarViewSet
app_name = "catalog"
router = DefaultRouter()
router.register("brands", BrandViewSet, basename="brand")
router.register("cars", CarViewSet, basename="car")
urlpatterns = router.urls
