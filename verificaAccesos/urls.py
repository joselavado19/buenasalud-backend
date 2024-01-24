from django.urls import path, include
from verificaAccesos.views import VerificaAccesosViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"verificaAccesos", VerificaAccesosViewSet)

urlpatterns = [
     path("", include(router.urls))
]