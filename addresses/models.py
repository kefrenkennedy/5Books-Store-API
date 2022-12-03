from django.db import models
import uuid


class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    street_name = models.TextField()
    district = models.TextField()
    number = models.IntegerField()
    zip_code = models.CharField(max_length=8)
    city = models.TextField()
    state = models.CharField(max_length=2)
    address_complement = models.TextField()
