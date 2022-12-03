from django.db import models
from django.core.validators import MaxValueValidator
import uuid


# Create your models here.
class TypeBooks(models.TextChoices):
    EBOOK = "E-book"
    BOOK = "Book"


class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=126)
    date_release = models.DateField()
    book_cover = models.URLField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    publishing_company = models.CharField(max_length=126)
    language = models.CharField(max_length=50)
    edition_number = models.CharField(max_length=50)
    number_pages = models.IntegerField()
    country = models.CharField(max_length=50)
    isbn = models.PositiveIntegerField(validators=[MaxValueValidator(13)])
    type = models.CharField(
        max_length=7, choices=TypeBooks.choices, default=TypeBooks.EBOOK
    )
    amount = models.PositiveIntegerField()
    weigth = models.PositiveIntegerField()
    format = models.PositiveIntegerField()
    length = models.DecimalField(max_digits=4, decimal_places=2)
    width = models.DecimalField(max_digits=4, decimal_places=2)
    diameter = models.PositiveIntegerField()

    author = models.ForeignKey(
        "authors.Author", on_delete=models.SET_NULL, related_name="books", null=True
    )

    category = models.ForeignKey(
        "categories.Categories", on_delete=models.CASCADE, related_name="books"
    )

    orders = models.ManyToManyField("orders.Order", related_name="books")
