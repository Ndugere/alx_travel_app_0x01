# core/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    shop_name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return f"{self.username} ({self.shop_name})" 

class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="categories") 

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="products"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="items"
    )
    name = models.CharField(max_length=60)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Products"
        ordering = ["name"]

    @property
    def in_stock(self):
        return self.quantity > 0

    def __str__(self):
        return f"{self.name} - {self.user.shop_name}"
