

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from . import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(self, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class MyTokenRefrshSerializer(TokenObtainPairSerializer):
    def get_token(self,user):
        token = super().get_token(user)
        token ['username'] = user.username
        return token

class MyTokenRefreshView(TokenObtainPairView):
    serializer_class = MyTokenRefrshSerializer

class RegisterView(CreateAPIView):
    serializer_class = serializers.RegisterSerializer


class LoginView(APIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            access_token = MyTokenObtainPairSerializer().get_token(user)
            refresh_token = RefreshToken.for_user(user)
            # MyTokenRefrshSerializer().update(refresh_token,{'user':user})
            valid_data = {
                'access_token': str(access_token.access_token),
                'refresh_token': str(refresh_token),
                'username': user.username,}
            
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST) 