from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class ProductAPIViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
