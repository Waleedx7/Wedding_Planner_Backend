from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializer(serializers.ModelSerializer):
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
    email = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        # email = data.get('email')
        try:
            user = User.objects.get(username=username)
            print(user.username)
        except User.DoesNotExist:
            print("This user doesn't exist")
        print(user)
        print(password)
        if not user.check_password(password):
            raise serializers.ValidationError('Incorrect credentials')
        
        payload = RefreshToken.for_user(user)
        data['access'] = str(payload.access_token)
        return data