from rest_framework.viewsets import ModelViewSet
from .models import RowVentasEspcialidad
from .serializers import RowVentasEspcialidadSerializer
##from rest_framework.permissions import IsAuthenticated


class RowVentasEspcialidadViewSet(ModelViewSet):
    queryset = RowVentasEspcialidad.objects.all()  # select * from subscription
    serializer_class = RowVentasEspcialidadSerializer
   ## permission_classes = [IsAuthenticated]