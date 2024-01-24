from django.urls import path, include
from gridVentasCompara.views import GridVentasComparaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"gridVentasCompara", GridVentasComparaViewSet)

urlpatterns = [
     path("", include(router.urls))
]