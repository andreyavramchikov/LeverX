from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'email', 'user_type', 'first_name', 'last_name', )


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'email', 'password', )
