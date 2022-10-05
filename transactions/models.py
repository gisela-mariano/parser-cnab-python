from django.db import models
from django.core.validators import MaxValueValidator
import uuid


class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.PositiveIntegerField(validators=[MaxValueValidator(9)])
    date = models.CharField(max_length=8)
    hour = models.CharField(max_length=6)
    value = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    store_owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)