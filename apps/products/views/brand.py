from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view
from rest_framework import mixins
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from apps.api_tags import BRAND_TAG
from apps.common.permissions import ACCESS_DENIED_ERROR
from apps.common.permissions import ReadOnlyAdminModifyPermission
from apps.common.permissions import UNAUTHORIZED_ERROR
from apps.products.models import Brand
from apps.products.serializers import BrandSerializer


@extend_schema_view(
    list=extend_schema(
        tags=[BRAND_TAG],
        summary=_('List all brands'),
        description=_('Retrieve a list of all brands'),
        responses={status.HTTP_200_OK: BrandSerializer(many=True)},
    ),
    retrieve=extend_schema(
        tags=[BRAND_TAG],
        summary=_('Retrieve a brand'),
        description=_('Retrieve a single brand by ID'),
        responses={status.HTTP_200_OK: BrandSerializer},
    ),
    update=extend_schema(
        tags=[BRAND_TAG],
        summary=_('Update a brand'),
        description=_('Update a brand with the provided data'),
        request=BrandSerializer,
        responses={
            status.HTTP_200_OK: BrandSerializer,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED_ERROR,
            status.HTTP_403_FORBIDDEN: ACCESS_DENIED_ERROR,
        },
    ),
    partial_update=extend_schema(
        tags=[BRAND_TAG],
        summary=_('Partial update a brand'),
        description=_('Partial update a brand with the provided data'),
        request=BrandSerializer,
        responses={
            status.HTTP_200_OK: BrandSerializer,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED_ERROR,
            status.HTTP_403_FORBIDDEN: ACCESS_DENIED_ERROR,
        },
    ),
    destroy=extend_schema(
        tags=[BRAND_TAG],
        summary=_('Delete a brand'),
        description=_('Delete a brand by ID'),
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED_ERROR,
            status.HTTP_403_FORBIDDEN: ACCESS_DENIED_ERROR,
        },
    ),
)
class BrandAPIViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (ReadOnlyAdminModifyPermission,)
