from rest_framework import serializers

from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

        extra_kwargs = {
            "user": {'required': False},
            "stars": {"min_value": 1, "max_value": 5}
        }


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

        read_only_fields = ["id", "book", 'user']

        extra_kwargs = {
            "stars": {"min_value": 1, "max_value": 5}
        }
