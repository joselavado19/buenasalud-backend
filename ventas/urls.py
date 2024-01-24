from django.urls import path, include
from ventas.views import VentasViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"ventas", VentasViewSet)

urlpatterns = [
     path("", include(router.urls))
]