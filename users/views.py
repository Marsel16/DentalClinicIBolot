from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import get_user_model, authenticate, login, logout
User = get_user_model()
class RegisterAPI(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data)
        user.save()
        login(request, user)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return redirect('/api/v1/reviews/')


class LoginAPI(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                return redirect('/api/v1/reviews/')
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'message': 'Email пользователя или пароль неверен!'})


class LogoutAPI(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response('Вы вышли из акаунта')

