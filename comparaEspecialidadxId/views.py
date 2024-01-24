from rest_framework.viewsets import ModelViewSet
from .models import ComparaEspecialidadxId
from .serializers import ComparaEspecialidadxIdSerializer
##from rest_framework.permissions import IsAuthenticated


class ComparaEspecialidadxIdViewSet(ModelViewSet):
    queryset = ComparaEspecialidadxId.objects.all()  # select * from subscription
    serializer_class = ComparaEspecialidadxIdSerializer
   ## permission_classes = [IsAuthenticated]