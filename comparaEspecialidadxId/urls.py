from django.urls import path, include
from comparaEspecialidadxId.views import ComparaEspecialidadxIdViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"comparaEspecialidadxId", ComparaEspecialidadxIdViewSet)

urlpatterns = [
     path("", include(router.urls))
]