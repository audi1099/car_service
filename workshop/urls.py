from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, CarViewSet, RepairOrderViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'cars', CarViewSet)
router.register(r'repair-orders', RepairOrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]