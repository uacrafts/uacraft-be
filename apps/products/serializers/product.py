from rest_framework import serializers

from apps.products.models import Product
from apps.products.serializers.brand import BrandSerializer
from apps.products.serializers.category import CategorySerializer
from apps.products.serializers.price import PriceSerializer
from apps.products.serializers.store import StoreSerializer


class ProductSerializer(serializers.ModelSerializer):
    store = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'pk',
            'title',
            'store',
            'price',
            'brand',
            'category',
            'image',
            'image_url',
            'description',
            'is_stock',
            'created_at',
            'updated_at'
        )
        read_only_fields = ('created_at', 'updated_at', 'image_url')

    def get_store(self, obj):
        if hasattr(obj, 'store'):
            return StoreSerializer(obj.store).data
        return None

    def get_price(self, obj):
        if hasattr(obj, 'price'):
            return PriceSerializer(obj.price).data
        return None

    def get_brand(self, obj):
        if hasattr(obj, 'brand'):
            return BrandSerializer(obj.brand).data
        return None

    def get_category(self, obj):
        if hasattr(obj, 'category'):
            return CategorySerializer(obj.category).data
        return None

    def get_image_url(self, obj):
        if hasattr(obj, 'image'):
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None
