from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.products.models import Category
from apps.products.serializers import CategorySerializer


class CategoryAPIViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
