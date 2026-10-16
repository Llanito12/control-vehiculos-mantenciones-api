from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehiculoViewSet, MantencionViewSet

router = DefaultRouter()
router.register(r'vehiculos', VehiculoViewSet, basename='vehiculo')
router.register(r'mantenciones', MantencionViewSet, basename='mantencion')

urlpatterns = [
    path('', include(router.urls)),
]