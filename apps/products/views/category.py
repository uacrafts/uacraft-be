from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view
from rest_framework import mixins
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from apps.api_tags import CATEGORY_TAG
from apps.common.permissions import ACCESS_DENIED_ERROR
from apps.common.permissions import ReadOnlyAdminModifyPermission
from apps.common.permissions import UNAUTHORIZED_ERROR
from apps.products.models import Category
from apps.products.serializers import CategorySerializer


@extend_schema_view(
    list=extend_schema(
        tags=[CATEGORY_TAG],
        summary=_('List all categories'),
        description=_('Retrieve a list of all categories'),
        responses={
            status.HTTP_200_OK: CategorySerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        tags=[CATEGORY_TAG],
        summary=_('Retrieve a category'),
        description=_('Retrieve a single category by ID'),
        responses={
            status.HTTP_200_OK: CategorySerializer,
        },
    ),
    update=extend_schema(
        tags=[CATEGORY_TAG],
        summary=_('Update a category'),
        description=_('Update a category with the provided data'),
        request=CategorySerializer,
        responses={
            status.HTTP_200_OK: CategorySerializer,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED_ERROR,
            status.HTTP_403_FORBIDDEN: ACCESS_DENIED_ERROR,
        },
    ),
    partial_update=extend_schema(
        tags=[CATEGORY_TAG],
        summary=_('Partial update a category'),
        description=_('Partial update a category with the provided data'),
        request=CategorySerializer,
        responses={
            status.HTTP_200_OK: CategorySerializer,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED_ERROR,
            status.HTTP_403_FORBIDDEN: ACCESS_DENIED_ERROR,
        },
    ),
    destroy=extend_schema(
        tags=[CATEGORY_TAG],
        summary=_('Delete a category'),
        description=_('Delete a category by ID'),
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_401_UNAUTHORIZED: UNAUTHORIZED_ERROR,
            status.HTTP_403_FORBIDDEN: ACCESS_DENIED_ERROR,
        },
    ),
)
class CategoryAPIViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (ReadOnlyAdminModifyPermission,)
