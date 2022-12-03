from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import Request, Response, status, APIView
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework.authtoken.models import Token
from .models import User
from .permissions import IsAdminOrUser, IsOwner
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import authenticate

import ipdb


class ListCreateUserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UpdateUserView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminOrUser, IsOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        try:
            userSelect = self.queryset.filter(id=self.kwargs["pk"])
            dataUpdate = {
                **request.data,
                "is_active": userSelect[0].is_active,
                "is_superuser": userSelect[0].is_superuser,
            }
            self.queryset.filter(id=self.kwargs["pk"]).update(**dataUpdate)
            userGet = self.queryset.get(id=self.kwargs["pk"])
            serial = UserSerializer(userGet)
            return Response(serial.data, status.HTTP_200_OK)
        except Exception:
            return Response({"detail": "User Not Found"})


class UpdateActiveView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        try:
            self.queryset.filter(id=self.kwargs["pk"]).update(
                is_active=request.data["is_active"]
            )
            userGet = self.queryset.get(id=self.kwargs["pk"])
            serial = UserSerializer(userGet)
            return Response(serial.data, status.HTTP_200_OK)
        except Exception:
            return Response({"detail": "User Not Found"})


class LoginView(APIView):
    def post(self, request: Request, *args, **kwargs):
        try:
            serializer = UserLoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = User.objects.get(username=serializer.data["username"])

            verifyPassword = authenticate(user, serializer.data["password"])

            if verifyPassword:
                token, created = Token.objects.get_or_create(user=user)

                return Response({"token": token.key})
            else:
                return Response(
                    {"detail": "invalid username or password"},
                    status.HTTP_401_UNAUTHORIZED,
                )

        except User.DoesNotExist:
            return Response(
                {"detail": "invalid username or password"}, status.HTTP_401_UNAUTHORIZED
            )
