from rest_framework.viewsets import ModelViewSet
from .models import Ventas
from .serializers import VentasSerializer
##from rest_framework.permissions import IsAuthenticated


class VentasViewSet(ModelViewSet):
    queryset = Ventas.objects.all()  # select * from subscription
    serializer_class = VentasSerializer
   ## permission_classes = [IsAuthenticated]