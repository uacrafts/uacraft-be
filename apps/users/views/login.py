from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from apps.api_tags import USER_TAG
from apps.users.serializers import LoginResponseSerializer
from apps.users.serializers import LoginSerializer


@extend_schema(
    tags=[USER_TAG],
    summary=_('User Login'),
    description=_('Authenticate user and retrieve access token along with email verification status.'),
    responses={status.HTTP_200_OK: LoginResponseSerializer},
)
class LoginAPIView(ObtainAuthToken):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data)
