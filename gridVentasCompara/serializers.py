from rest_framework.serializers import ModelSerializer
from .models import GridVentasCompara



class GridVentasComparaSerializer(ModelSerializer):
    class Meta:
        model = GridVentasCompara
        fields = "__all__"