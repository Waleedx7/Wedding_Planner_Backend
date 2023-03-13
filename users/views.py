

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from . import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


class RegisterView(CreateAPIView):
    serializer_class = serializers.RegisterSerializer


class LoginView(APIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST) 