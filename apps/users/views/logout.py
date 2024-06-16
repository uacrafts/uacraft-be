from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import OpenApiResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api_tags import USER_TAG
from apps.users.serializers import LogOutSerializer


@extend_schema(
    tags=[USER_TAG],
    summary=_('User Logout'),
    description=_('Invalidate the user access token to log them out.'),
    responses={
        status.HTTP_204_NO_CONTENT: OpenApiResponse(description=_('Logged out successfully.')),
        status.HTTP_401_UNAUTHORIZED: OpenApiResponse(description=_('Unauthorized. Token not found or invalid.')),
    },
)
class LogoutAPIView(APIView):
    serializer_class = LogOutSerializer

    def post(self, request, *args, **kwargs):
        auth_token = request.headers.get('Authorization', '').split(' ')[1]

        try:
            token = Token.objects.get(key=auth_token)
        except Token.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        token.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
