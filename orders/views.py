from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from rest_framework.authentication import TokenAuthentication
from .permissions import isUserOrAdmin
from rest_framework.views import Response, status
import ipdb
from django.shortcuts import get_object_or_404
from books.models import Book


class OrderListAndCreateViews(generics.ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [isUserOrAdmin]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer(
            data=request.data,
            context={"user": request.user},
            many=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # ipdb.set_trace()
        list_books = []
        for index, _ in enumerate(serializer.data):
            list_books.append(request.data[index]['books'])

        new_serializer = {
            "id": serializer.data[0]['id'],
            "status": serializer.data[0]['status'],
            'books': list_books,
            "shipping": serializer.data[0]['shipping'],
            "ammount_items": serializer.data[0]['ammount_items'],
            "total_value": serializer.data[0]['total_value'],
            "user": serializer.data[0]['user'],
        }

        return Response(new_serializer, status.HTTP_201_CREATED)
