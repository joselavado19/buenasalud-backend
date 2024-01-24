from rest_framework.serializers import ModelSerializer
from .models import RowVentasEspcialidad



class RowVentasEspcialidadSerializer(ModelSerializer):
    class Meta:
        model = RowVentasEspcialidad
        fields = "__all__"