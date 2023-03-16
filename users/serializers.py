from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True) 
   
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data) 
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, valid_data):
        username = valid_data.get('username')
        password = valid_data.get('password')
       
       
        try:
            user = User.objects.get(username=username)
           
        except User.DoesNotExist:
            print("This user doesn't exist")
      
        if not user.check_password(password):
            raise serializers.ValidationError('Incorrect credentials')
        
        refresh_token = RefreshToken.for_user(user)
        access_token = refresh_token.access_token
        valid_data['access'] = str(access_token)
        valid_data['refresh'] = str(refresh_token)
        valid_data['user'] = user
        return valid_data