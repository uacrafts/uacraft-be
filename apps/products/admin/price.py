from django.contrib import admin

from apps.products.models import Price


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    ...
