from drf_spectacular.utils import extend_schema_field
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
            'id',
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

    @extend_schema_field(StoreSerializer)
    def get_store(self, product: Product):
        if product.store:
            return StoreSerializer(product.store).data
        return None

    @extend_schema_field(PriceSerializer)
    def get_price(self, product: Product):
        if product.price:
            return PriceSerializer(product.price).data
        return None

    @extend_schema_field(BrandSerializer)
    def get_brand(self, product: Product):
        if product.brand:
            return BrandSerializer(product.brand).data
        return None

    @extend_schema_field(CategorySerializer)
    def get_category(self, product: Product):
        if product.category:
            return CategorySerializer(product.category).data
        return None

    @extend_schema_field(serializers.CharField)
    def get_image_url(self, product: Product):
        if product.image:
            return self.context['request'].build_absolute_uri(product.image.url)
        return None
