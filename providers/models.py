from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Provider(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    language = models.CharField(max_length=10)
    currency = models.CharField(max_length=10)
