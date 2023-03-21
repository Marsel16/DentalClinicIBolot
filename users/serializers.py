from django.shortcuts import redirect
from rest_framework import serializers, status
from rest_framework.serializers import *
from rest_framework.validators import UniqueValidator
from phonenumber_field.serializerfields import PhoneNumberField
from django.contrib.auth.password_validation import validate_password
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'phone_number', 'first_name', 'last_name', 'password')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    phone_number = PhoneNumberField(default='+996', min_length=12, max_length=13,
                                    validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = CharField(max_length=128)
    last_name = CharField(max_length=128)
    password = serializers.CharField(min_length=8, max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'phone_number', 'first_name', 'last_name', 'password']
        extra_kwargs = {"password": {'write_only': True}}

    def valivalidate_password(self, value):
        validate_password(value)
        return value


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['token']
