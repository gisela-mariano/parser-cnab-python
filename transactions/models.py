from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator
import uuid


class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.PositiveIntegerField(validators=[MaxValueValidator(9), MinLengthValidator(1)])
    date = models.CharField(max_length=8, validators=[MinLengthValidator(8)])
    hour = models.CharField(max_length=6, validators=[MinLengthValidator(6)])
    value = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    card = models.CharField(max_length=12, validators=[MinLengthValidator(12)])
    store_owner = models.CharField(max_length=14, validators=[MinLengthValidator(14)])
    store_name = models.CharField(max_length=19, validators=[MinLengthValidator(19)])