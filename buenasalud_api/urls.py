from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(
        title="BuenaSalud api",
        default_version="v1",
        description="ApI basado en BuenaSalud",
        license=openapi.License(name="MIT")
    ),
    public=True,
    permission_classes=(AllowAny,)
)


api_version = "api/v1/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(api_version, include("ventas.urls")),
    path(api_version, include("rowVentasEspcialidad.urls")),
    path(api_version, include("gridVentasCompara.urls")),
    path(api_version, include("comparaEspecialidadxId.urls")),
    path(api_version, include("listEspecialidad.urls")),
    path(api_version, include("verificaAccesos.urls")),
    path(api_version, include("user.urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui')
]
