from rest_framework.serializers import ModelSerializer
from .models import ListEspecialidad



class ListEspecialidadSerializer(ModelSerializer):
    class Meta:
        model = ListEspecialidad
        fields = "__all__"