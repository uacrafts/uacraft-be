from django.contrib import admin

from apps.products.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    ...
