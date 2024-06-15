from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import OpenApiResponse
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.api_tags import USER_TAG
from apps.users.serializers.confirm_email_complete import ConfirmEmailCompleteSerializer
from apps.users.serializers.confirm_email_complete import ConfirmEmailSerializer


@extend_schema(
    tags=[USER_TAG],
    summary=_('Confirm email completion'),
    description=_('This endpoint confirms the user\'s email address using the provided UID and token.'),
    responses={
        status.HTTP_200_OK: ConfirmEmailCompleteSerializer,
        status.HTTP_400_BAD_REQUEST: OpenApiResponse(description=_('Invalid token or uid')),
    }
)
class ConfirmEmailCompleteView(GenericAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    serializer_class = ConfirmEmailCompleteSerializer

    def get(self, request, *args, **kwargs):
        serializer = ConfirmEmailSerializer(
            data={
                'uid': self.kwargs['uid'],
                'token': self.kwargs['token'],
            }
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        serializer = self.get_serializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)
