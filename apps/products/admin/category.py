from django.contrib import admin

from apps.products.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'slug', 'created_at', 'updated_at')
    fields = ('title', 'parent', 'slug', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
