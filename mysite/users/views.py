from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from .models import Users
from .serializers import RegisterSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Пользователь создан"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        login = request.data.get('login')
        password = request.data.get('password')

        try:
            user = Users.objects.get(login=login)
        except Users.DoesNotExist:
            return Response({"error": "Пользователь не найден"}, status=status.HTTP_401_UNAUTHORIZED)

        if check_password(password, user.password):
            # Создаём/получаем токен
            token, _ = Token.objects.get_or_create(user_id=user.id)
            return Response({"token": token.key})

        return Response({"error": "Неверный пароль"}, status=status.HTTP_401_UNAUTHORIZED)
