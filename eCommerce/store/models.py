from django.db import models
from django.db.models import Model
from django.contrib.auth.models import AbstractUser


class TheUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    imageUrl = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(TheUser, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, blank=True)
