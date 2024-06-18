from django.contrib import admin

from apps.products.models import Seller


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
