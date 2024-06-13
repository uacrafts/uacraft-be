from django.contrib import admin

from apps.products.models import Store


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    ...
