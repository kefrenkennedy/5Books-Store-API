from rest_framework import serializers

from cards.models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["id", "user", "card_name", "number_card", "expire_date"]
        read_only_fields = ["id", "user"]


class CardGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["id", "card_name", "number_card", "expire_date"]
        read_only_fields = ["id"]
