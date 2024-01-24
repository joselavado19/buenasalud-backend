from django.urls import path, include
from rowVentasEspcialidad.views import RowVentasEspcialidadViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"rowVentasEspcialidad", RowVentasEspcialidadViewSet)

urlpatterns = [
     path("", include(router.urls))
]