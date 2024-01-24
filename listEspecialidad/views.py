from rest_framework.viewsets import ModelViewSet
from .models import ListEspecialidad
from .serializers import ListEspecialidadSerializer
##from rest_framework.permissions import IsAuthenticated


class ListEspecialidadViewSet(ModelViewSet):
    queryset = ListEspecialidad.objects.all()  # select * from subscription
    serializer_class = ListEspecialidadSerializer
   ## permission_classes = [IsAuthenticated]