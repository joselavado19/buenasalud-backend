from django.urls import path, include
from verificaAccesos.views import VerificaAccesosViewSet
from .views import LoginView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"verificaAccesos", VerificaAccesosViewSet)


urlpatterns = [
     path("", include(router.urls)),
     path("login", LoginView.as_view()),
]