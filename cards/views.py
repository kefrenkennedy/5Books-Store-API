from django.shortcuts import render
from rest_framework import generics
from .models import Card
from .serializers import CardSerializer, CardGetSerializer
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdminOrUser, HasObjectPermissionOrIsAdmin
import ipdb

##GET POST PATCH DELETE


class CardGetPostViews(generics.ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrUser]

    queryset = Card.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CardGetSerializer
        return CardSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CardUpdateDeleteViews(generics.UpdateAPIView, generics.DestroyAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [HasObjectPermissionOrIsAdmin]

    queryset = Card.objects.all()
    serializer_class = CardGetSerializer
