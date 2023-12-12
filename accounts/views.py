from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer


class UserRegistrationView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes=(AllowAny,)

    def perform_create(self, serializer):
        password = serializer.validated_data.get('password')
        hashed_password = make_password(password)
        serializer.save(password=hashed_password)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            print(refresh_token,"anzil")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetUpdateProfile(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser
    permission_classes = (IsAuthenticated,)
    

class ChangePassword(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        user = request.user
        if not user:
            raise PermissionDenied("User not found.")


        old_password = request.data.get('current_password')
        new_password = request.data.get('new_password')

        print(old_password,"old_password")
        print(new_password,"new_password")


        
        if not old_password or not new_password:
            return Response({'error': 'Both old and new passwords are required.'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(old_password):
            return Response({'error': 'Invalid old password.'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)



