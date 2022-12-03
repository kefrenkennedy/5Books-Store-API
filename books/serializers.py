from rest_framework.serializers import ModelSerializer
from .models import Book
from authors.serializers import AuthorSerializer
from authors.models import Author
from categories.serializers import CategoriesSerializer
import ipdb


class BookSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategoriesSerializer(read_only=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "name",
            "author",
            "category",
            "date_release",
            "book_cover",
            "price",
            "description",
            "publishing_company",
            "language",
            "edition_number",
            "number_pages",
            "country",
            "isbn",
            "type",
            "amount",
            "weigth",
            "format",
            "length",
            "width",
            "diameter",
        ]

    read_only_fields = ["id"]


class EbookSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategoriesSerializer(read_only=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "name",
            "author",
            "category",
            "date_release",
            "book_cover",
            "price",
            "description",
            "publishing_company",
            "language",
            "edition_number",
            "number_pages",
            "country",
            "isbn",
            "type",
        ]

        read_only_fields = ["id"]
