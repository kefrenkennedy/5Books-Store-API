from django.db import models
import uuid
from correios_utils import (
    Cotacao,
    FormatoEncomenda,
    SimNao,
    Servico,
    realizar_cotacao,
    get_descricao_servico,
)
from users.serializers import UserSerializer
from books.serializers import BookSerializer


class Status_Order(models.TextChoices):
    ORDER_CREATED = "Order created"
    PROCESS_PAYMENT = "Process payment"
    AUTHORIZED_PAYMENT = "Authorized payment"
    WAITING_SHIPPING = "Waiting Shipping"
    SENT = "Sent"
    ORDER_COMPLETED = "Order completed"


class Order(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    status = models.CharField(
        choices=Status_Order.choices, default=Status_Order.ORDER_CREATED, max_length=40
    )

    shipping = models.IntegerField(null=False)
    ammount_items = models.IntegerField(null=False)
    total_value = models.IntegerField(null=False)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="orders"
    )
