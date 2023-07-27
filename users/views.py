from time import sleep
import jwt
import requests
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer, PrivateUserSerializer
from users.models import User
from . import serializers


# Create your views here.
class Users(APIView):
    def get(self, request):
        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return Response(serializer.data)

    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError()
        serializer = serializers.PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class PublicUser(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound
        serializer = serializers.PrivateUserSerializer(user)
        return Response(serializer.data)


class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        if not old_password or not new_password:
            raise ParseError
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            raise ParseError


class LogIn(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return Response({"ok": "Welcome!"})
        else:
            return Response(
                {"error": "wrong password"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class LogOut(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        sleep(5)
        logout(request)
        return Response({"ok": "bye!"})


class JWTLogIn(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            token = jwt.encode(
                {"pk": user.pk},
                settings.SECRET_KEY,
                algorithm="HS256",
            )
            return Response({"token": token})
        else:
            return Response({"error": "wrong password"})


class SignUp(APIView):
    # from django.contrib.auth import authenticate의 authenticate는 username과 password이 맞다면 두 가지를 돌려주는 function.
    # 그리고 토큰과 쿠키를 받아와서 자동으로 생성 등을 해준다. 그래서 request가 같이 필요한 듯?

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        name = request.data.get("name")
        email = request.data.get("email")
        # Signup 시에는 username, password, name, email을 받아와야 한다.
        # 그리고 먼저 데이터베이스에 접근해 username과 email이 이미 존재하는지 확인해야 한다.

        try:
            if not username or not password or not name or not email:
                raise Response(
                    {"error": "All fields are required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if User.objects.filter(username=username).exists():
                return Response(
                    {"error": "Username already exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if User.objects.filter(email=email).exists():
                return Response(
                    {"error": "Email already exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                name=name,
            )
            user.save()
            login(request, user)
            return Response({"ok": "Welcome!"})
        except ParseError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
