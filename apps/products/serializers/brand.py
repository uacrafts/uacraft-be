from rest_framework import serializers

from apps.products.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'title',
            'created_at',
            'updated_at'
        )

        read_only_fields = ('created_at', 'updated_at')
