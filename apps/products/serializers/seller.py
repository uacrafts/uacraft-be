from rest_framework import serializers

from apps.products.models import Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = (
            'id',
            'title',
            'city',
            'is_displayed',
            'created_at',
            'updated_at'
        )
        read_only_fields = ('created_at', 'updated_at')
