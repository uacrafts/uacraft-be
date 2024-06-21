from django.contrib import admin

from apps.products.admin.inlines import ProductImageInline
from apps.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
