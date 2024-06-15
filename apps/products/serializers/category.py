from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from apps.products.models import Category


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'slug',
            'parent',
            'created_at',
            'updated_at'
        )
        read_only_fields = ('slug', 'created_at', 'updated_at')

    @staticmethod
    def get_parent(category: Category) -> 'CategorySerializer':
        if category.parent:
            return CategorySerializer(category.parent).data
        return None
