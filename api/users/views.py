from rest_framework import viewsets
from .serializers import CreateUserSerializer,CustomSigninSerializer,SearchAPISerializer
from .models import CustomUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import permissions

# Create your views here.
class CreateUserView(viewsets.ModelViewSet):
    serializer_class = CreateUserSerializer
    queryset = CustomUser.objects.all()
    http_method_names = ['post']
    permission_classes = [permissions.AllowAny]

class SearchAPIView(APIView):
    def get(self,request,email):
        queryset = CustomUser.objects.filter(email__icontains = email)
        serializer = SearchAPISerializer(queryset,many=True)
        return Response(serializer.data)

class GenerateTokenView(APIView):
    serializer_class = CustomSigninSerializer
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data.pop('password')
            email = serializer.validated_data.pop('email')
            user = authenticate(email = email, password = password)
            if user:
                token,_ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key,'is_staff': user.is_staff,'is_lead': user.is_lead,'email': user.email})
            return Response({'error': "user not found"},status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.errors)
