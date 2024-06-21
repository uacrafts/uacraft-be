from django.db import transaction
from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import OpenApiResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.api_tags import USER_TAG
from apps.users.serializers import RegistrationSerializer
from apps.users.tasks import send_email_confirmation


@extend_schema(
    tags=[USER_TAG],
    summary=_('Register a new user'),
    description=_('Allows you to register a new user. On successful registration, an email confirmation is sent.'),
    request=RegistrationSerializer,
    responses={
        status.HTTP_204_NO_CONTENT: OpenApiResponse(description=_('The user is successfully registered.')),
        status.HTTP_400_BAD_REQUEST: OpenApiResponse(description=_('Invalid or missing user credentials.')),
    }
)
class RegistrationAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            user = serializer.save()
            transaction.on_commit(lambda: send_email_confirmation(user_id=user.pk))

        return Response(status=status.HTTP_204_NO_CONTENT)
