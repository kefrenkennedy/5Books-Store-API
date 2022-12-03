from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .serializers import Address, SerializerAddress
from .permissions import IsOwnerOrReadOnly


class AdressDetail(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Address.objects
    serializer_class = SerializerAddress
