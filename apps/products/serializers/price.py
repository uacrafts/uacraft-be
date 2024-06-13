from rest_framework import serializers

from apps.products.models import Price


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = (
            'pk',
            'regular_price',
            'special_price',
            'discount_percentage',
        )
        read_only_fields = ('discount_percentage',)
