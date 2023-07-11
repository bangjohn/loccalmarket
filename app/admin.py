from django.contrib import admin
from .models import Product, ProductVariation


# Register your models here.
@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = (
        "name",
        "purchase_price",
        "selling_price",
        "stock",
        "slug",
        "supplier_link",
    )
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)


@admin.register(ProductVariation)
class ProductVariation(admin.ModelAdmin):
    list_display = ("product", "price", "stock")
    list_filter = ("product",)
    search_fields = ("product__name", "variation_name")


# @admin.register(TemporaryImage)
# class TemporaryImage(admin.ModelAdmin):
#     list_display = ('image', 'uploaded_at')
