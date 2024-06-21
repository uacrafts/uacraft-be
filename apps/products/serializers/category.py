from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from apps.products.models import Category


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'created_at', 'updated_at')


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

    @extend_schema_field(ParentSerializer)
    def get_parent(self, category: Category) -> dict[str, any] | None:
        if category.parent:
            return ParentSerializer(category.parent).data
        return None
