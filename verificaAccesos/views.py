from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import VerificaAccesos
from .serializers import VerificaAccesosSerializer
from django.contrib.auth.models import User
##from rest_framework.permissions import IsAuthenticated


class VerificaAccesosViewSet(ModelViewSet):
    queryset = VerificaAccesos.objects.all()  # select * from subscription 
    serializer_class = VerificaAccesosSerializer
   ## permission_classes = [IsAuthenticated]
    
class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = VerificaAccesos.objects.filter(username=username).first()
        
        if user is None:
            raise AuthenticationFailed('User no encontrado')
        
           
        if not User.check_password(password,user.password):
            raise AuthenticationFailed('Password Incorrecto')
        
        return Response({
            'message': 'success'
        })
    
    