# models.py
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/", blank=True)
    category = models.CharField(
        max_length=255,
        choices=[
            ("Electronics", "Electronics"),
            ("Fashion", "Fashion"),
            ("Home Goods", "Home Goods"),
            ("Toys", "Toys"),
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
