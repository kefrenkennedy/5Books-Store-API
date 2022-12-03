from rest_framework import serializers
from rest_framework.views import Response, status
from orders.models import Order
from books.models import Book
from users.serializers import UserSerializer
from books.serializers import BookSerializer
from books.models import Book
from .utils.fun_util import frete
import ipdb
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404


class OrderSerializer(serializers.ModelSerializer):
    books = serializers.UUIDField()

    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "books",
            "shipping",
            "ammount_items",
            "total_value",
            "user",
        ]

        read_only_fields = [
            "id",
            "status",
            "shipping",
            "total_value",
            "user",
        ]

    def create(self, validated_data):
        obj = {
            'user': self.context['user'],
            'data': self.initial_data
        }

        shipping_value, medidas = frete(**obj)
        # for obj_book in self.initial_data:
        for obj_book in self.initial_data:
            if obj_book.get('books'):
                book = get_object_or_404(Book, id=obj_book.get('books'))
                data = {
                    'shipping': shipping_value[0].valor,
                    'ammount_items': medidas['quantidade'],
                    'total_value': medidas['preco_total'],
                    'user_id': self.context['user'].id,
                }
                created_order = Order.objects.create(**data)
                created_order.books.add(book)

        return created_order
