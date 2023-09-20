from django.shortcuts import render
from .serializers import LoginSerializer, RegisterSerializer, LogoutSerializer, UserListSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from rest_framework.parsers import MultiPartParser

# Create your views here.


class RegisterView(generics.GenericAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = RegisterSerializer
    parser_classes = [MultiPartParser]  

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            resp = {
                'email': serializer.data.get('email')
            }
            return Response(resp, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    """API View: Login USER"""

    authentication_classes = []
    permission_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError("Incorrect Email/password.")

            refresh = RefreshToken.for_user(user)

            resp = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "msg": "Login Successfully"
            }
            print(resp,"========>>>>>>")
            return Response(resp, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LogoutSerializer

    def post(self, request):

        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            try:
                refresh_token = serializer.data.get('refresh_token')
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response("User Logged out successfully.", status=status.HTTP_200_OK)
            except Exception as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = UserListSerializer
    queryset = CustomUser.objects.all()

    def get(self, request, fullname=""):

        if fullname:
            users = self.get_queryset().filter(fullname=fullname)
        else:
            users = self.get_queryset()

        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
