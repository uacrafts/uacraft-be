from django.contrib import admin

from apps.products.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    fields = ('title', 'logo', 'description', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
