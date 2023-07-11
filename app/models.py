import os
import uuid
import random
import string


from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    description = models.TextField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    supplier_link = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


class ProductVariation(models.Model):
    SIZE_CHOICES = (
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    )
    COLOR_CHOICES = (
        ("R", "Red"),
        ("G", "Green"),
        ("B", "Blue"),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    color = models.CharField(max_length=1, choices=COLOR_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.size} - {self.color}"


class TemporaryImage(models.Model):
    folder_name = models.CharField(max_length=8, unique=True)
    image = models.ImageField(upload_to="")
    uploaded_at = models.DateTimeField(auto_now_add=True)
