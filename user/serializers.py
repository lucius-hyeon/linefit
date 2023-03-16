from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework import serializers
from .models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # ...

        return token
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('email',)
        extra_kwargs = {
            'password': {'write_only': True},
            "email": {"error_messages": {"required": "Give yourself a email"}}
        }


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # 패스워드는 읽으면 안되므로 쓰기작업만 허용
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user