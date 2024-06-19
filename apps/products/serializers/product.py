from typing import List

from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from apps.products.models import Product
from apps.products.models import ProductImage
from apps.products.serializers.brand import BrandSerializer
from apps.products.serializers.category import CategorySerializer
from apps.products.serializers.price import PriceSerializer
from apps.products.serializers.seller import SellerSerializer


class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    image_urls = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'seller',
            'price',
            'brand',
            'category',
            'image_urls',
            'description',
            'quantity_in_stock',
            'created_at',
            'updated_at'
        )
        read_only_fields = ('created_at', 'updated_at', 'image_urls')

    @extend_schema_field(SellerSerializer)
    def get_seller(self, product: Product) -> dict[str, any] | None:
        if product.seller:
            return SellerSerializer(product.seller).data
        return None

    @extend_schema_field(BrandSerializer)
    def get_brand(self, product: Product) -> dict[str, any] | None:
        if product.brand:
            return BrandSerializer(product.brand).data
        return None

    @extend_schema_field(PriceSerializer)
    def get_price(self, product: Product) -> dict[str, any] | None:
        if product.price:
            return PriceSerializer(product.price).data
        return None

    @extend_schema_field(CategorySerializer)
    def get_category(self, product: Product) -> dict[str, any] | None:
        if product.category:
            return CategorySerializer(product.category).data
        return None

    @extend_schema(
        description=_('List of image URLs for the product.'),
        responses=serializers.ListField(child=serializers.CharField())
    )
    def get_image_urls(self, product: Product) -> List[str]:
        request = self.context.get('request')
        return [request.build_absolute_uri(image.image.url) for image in product.product_images.all()]
