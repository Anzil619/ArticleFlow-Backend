from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email','password', 'phone', 'dob','is_superuser')

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)

        token['user_data'] = {
            'id' : user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone': user.phone,
            'dob': user.dob.strftime('%Y-%m-%d'),
            'is_superuser':user.is_superuser,
        }

        return token
    

    