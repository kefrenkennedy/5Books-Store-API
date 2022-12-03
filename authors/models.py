from django.db import models
import uuid

from traitlets import default

# Create your models here.

class Author(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=127, unique=True)