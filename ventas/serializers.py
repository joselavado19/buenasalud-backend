from rest_framework.serializers import ModelSerializer
from .models import Ventas



class VentasSerializer(ModelSerializer):
    class Meta:
        model = Ventas
        fields = "__all__"