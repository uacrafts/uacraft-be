from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view
from rest_framework import mixins
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from apps.api_tags import PRODUCT_TAG
from apps.common.permissions import ACCESS_DENIED_ERROR
from apps.common.permissions import ReadOnlyAdminModifyPermission
from apps.common.permissions import UNAUTHORIZED_ERROR
from apps.products.models import Product
from apps.products.serializers import ProductSerializer


@extend_schema_view(
    list=extend_schema(
        tags=[PRODUCT_TAG],
        summary=_('List all products'),
        description=_('Retrieve a list of all products'),
        responses={status.HTTP_200_OK: ProductSerializer(many=True)},
    ),
    retrieve=extend_schema(
        tags=[PRODUCT_TAG],
        summary=_('Retrieve a product'),
        description=_('Retrieve a single product by ID'),
        responses={status.HTTP_200_OK: ProductSerializer},
    ),
    update=extend_schema(
        tags=[PRODUCT_TAG],
        summary=_('Update a product'),
        description=_('Update a product with the provided data'),
        request=ProductSerializer,
        responses={
            status.HTTP_200_OK: ProductSerializer,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED_ERROR,
            status.HTTP_403_FORBIDDEN: ACCESS_DENIED_ERROR,
        },
    ),
    partial_update=extend_schema(
        tags=[PRODUCT_TAG],
        summary=_('Partial update a product'),
        description=_('Partial update a product with the provided data'),
        request=ProductSerializer,
        responses={
            status.HTTP_200_OK: ProductSerializer,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED_ERROR,
            status.HTTP_403_FORBIDDEN: ACCESS_DENIED_ERROR,
        },
    ),
    destroy=extend_schema(
        tags=[PRODUCT_TAG],
        summary=_('Delete a product'),
        description=_('Delete a product by ID'),
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED_ERROR,
            status.HTTP_403_FORBIDDEN: ACCESS_DENIED_ERROR,
        },
    ),
)
class ProductAPIViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = Product.objects.all().select_related('brand', 'seller', 'price', 'category')
    serializer_class = ProductSerializer
    permission_classes = (ReadOnlyAdminModifyPermission,)
