from rest_framework.response import Response
from rest_framework import generics
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from users import serializers

# Create your views here.
class RegisterView(CreateAPIView):
    serializer_class = serializers.RegisterSerializer

class LoginView(APIView):
    serializer_class = serializers.LoginSerializer
    # permission_classes = []
    # authentication_classes = []
        
    def post(self, request):
        serializers = serializers.LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_user = serializer.data
            return Response(new_user, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)