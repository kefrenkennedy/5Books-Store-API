from .models import Categories
from rest_framework.authentication import TokenAuthentication
from .serializers import CategoriesSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class CategoriesListAndCreateViews(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]

    permission_classes = [IsAdminUser]
    queryset = Categories.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CategoriesSerializer
        return CategoriesSerializer


class CategoriesPatchDestroyViews(generics.UpdateAPIView, generics.DestroyAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer