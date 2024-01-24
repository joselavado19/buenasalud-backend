from rest_framework.viewsets import ModelViewSet
from .models import VerificaAccesos
from .serializers import VerificaAccesosSerializer
##from rest_framework.permissions import IsAuthenticated


class VerificaAccesosViewSet(ModelViewSet):
    queryset = VerificaAccesos.objects.all()  # select * from subscription
    serializer_class = VerificaAccesosSerializer
   ## permission_classes = [IsAuthenticated]