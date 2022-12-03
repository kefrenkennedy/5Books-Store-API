from django.db import models
import uuid


class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    stars = models.PositiveIntegerField()
    rating = models.CharField(max_length=600)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews"
    )

    book = models.ForeignKey(
        "books.Book", on_delete=models.SET_NULL, related_name="reviews", null=True
    )
