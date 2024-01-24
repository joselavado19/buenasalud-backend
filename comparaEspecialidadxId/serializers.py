from rest_framework.serializers import ModelSerializer
from .models import ComparaEspecialidadxId



class ComparaEspecialidadxIdSerializer(ModelSerializer):
    class Meta:
        model = ComparaEspecialidadxId
        fields = "__all__"