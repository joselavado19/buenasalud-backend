from rest_framework.viewsets import ModelViewSet
from .models import GridVentasCompara
from .serializers import GridVentasComparaSerializer
##from rest_framework.permissions import IsAuthenticated


class GridVentasComparaViewSet(ModelViewSet):
    queryset = GridVentasCompara.objects.all()  # select * from subscription
    serializer_class = GridVentasComparaSerializer
   ## permission_classes = [IsAuthenticated]