from django.urls import path, include
from listEspecialidad.views import ListEspecialidadViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"listEspecialidad", ListEspecialidadViewSet)

urlpatterns = [
     path("", include(router.urls))
]