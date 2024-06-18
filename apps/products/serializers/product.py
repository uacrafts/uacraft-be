from typing import Type

from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from apps.products.models import Product
from apps.products.serializers.brand import BrandSerializer
from apps.products.serializers.category import CategorySerializer
from apps.products.serializers.price import PriceSerializer
from apps.products.serializers.product_image import ProductImageSerializer
from apps.products.serializers.store import StoreSerializer


class ProductSerializer(serializers.ModelSerializer):
    store = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    images = ProductImageSerializer(many=True, read_only=True)
    image_urls = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'store',
            'price',
            'brand',
            'category',
            'images',
            'image_urls',
            'description',
            'is_stock',
            'created_at',
            'updated_at'
        )
        read_only_fields = ('created_at', 'updated_at', 'image_url')

    @extend_schema_field(StoreSerializer)
    def get_store(self, product: Product) -> dict[str, any] | None:
        if product.store:
            return StoreSerializer(product.store).data
        return None

    @extend_schema_field(PriceSerializer)
    def get_price(self, product: Product) -> dict[str, any] | None:
        if product.price:
            return PriceSerializer(product.price).data
        return None

    @extend_schema_field(BrandSerializer)
    def get_brand(self, product: Product) -> dict[str, any] | None:
        if product.brand:
            return BrandSerializer(product.brand).data
        return None

    @extend_schema_field(CategorySerializer)
    def get_category(self, product: Product) -> dict[str, any] | None:
        if product.category:
            return CategorySerializer(product.category).data
        return None

    @extend_schema_field(Type[list[str]])
    def get_image_urls(self, product: Product) -> list[str]:
        request = self.context.get('request')
        if not request:
            return []

        image_urls = []
        for image in product.images.all():
            image_urls.append(request.build_absolute_uri(image.image.url))
        return image_urls
