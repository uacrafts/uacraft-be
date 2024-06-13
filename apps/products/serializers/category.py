from rest_framework import serializers

from apps.products.models import Category


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'pk',
            'title',
            'slug',
            'parent',
            'created_at',
            'updated_at'
        )
        read_only_fields = ('slug', 'created_at', 'updated_at')

    def get_parent(self, obj):
        if obj.parent:
            return CategorySerializer(obj.parent).data
        return None
