from rest_framework.serializers import ModelSerializer
from .models import VerificaAccesos



class VerificaAccesosSerializer(ModelSerializer):
    class Meta:
        model = VerificaAccesos
        fields = "__all__"