from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        min_length=8
    )

    def validate(self, data):
        if data['password'] == 'contraseña':
            raise serializers.ValidationError("Usa una contraseña más segura")
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid Credentials')
        self.context['user'] = user

        return data

    def create(self, data):
        user = self.context['user']
        token, created_token = Token.objects.get_or_create(user=user)

        return token.key
