from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    access_token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password','confirm_password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    # def validate(self, data):
    #     if data ['password'] != data.pop('confirm_password'):
    #         raise serializers.ValidationError("Passwords must match")
    #     return data
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()        
        return user
    
   
    
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    # access_token = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        try:
            user = User.objects.get(username=username)
            print(user.username)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")
        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect password")
        return data
        
    # def get_access_token(self,access_token):
    #     payload = RefreshToken.for_user(access_token)
    #     token = str(payload.access_token)
    #     access_token['access_token'] = token
    #     return access_token
        
        # access_token = RefreshToken.for_user(user)
        # data['access_token'] = str(access_token.access_token)
        # return data
