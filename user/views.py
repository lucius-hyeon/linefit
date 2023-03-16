from user.serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import User
from .serializers import UserSerializer,CreateUserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
    
class UserView(APIView):
    
    def post(self, request):
        serializer = CreateUserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"회원가입 완료!"},status=status.HTTP_201_CREATED)
        return Response({"msg":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    

class UserInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many = True)

        return Response(serializer.data)