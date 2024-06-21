from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.translation import gettext_lazy as _
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from apps.users.utils.security import decode_uid

User = get_user_model()


class ConfirmEmailSerializer(serializers.Serializer):
    uid = serializers.CharField(required=True)
    token = serializers.CharField(required=True)

    def validate(self, attrs: dict) -> dict:
        uid = attrs['uid']
        token = attrs['token']

        try:
            user_id = decode_uid(uid)
            user = User.objects.get(pk=user_id)
        except (User.DoesNotExist, ValueError, TypeError, OverflowError):
            raise serializers.ValidationError(
                {'uid': _('Invalid uid')},
                code='invalid_uid',
            )

        if user.is_email_verified:
            raise serializers.ValidationError(
                {'uid': _('Email is already verified')},
                code='email_already_verified',
            )

        if not default_token_generator.check_token(user, token):
            raise serializers.ValidationError(
                {'token': _('Token is invalid')},
                code='token_invalid',
            )

        attrs['user'] = user
        return attrs

    def create(self, validated_data: dict) -> User:
        user = validated_data['user']
        user.is_email_verified = True
        user.save(update_fields=['is_email_verified'])
        return user


class ConfirmEmailCompleteSerializer(serializers.ModelSerializer):
    access_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'is_active',
            'access_token',
        )

    @extend_schema_field(OpenApiTypes.STR)
    def get_access_token(self, user: User) -> str:
        token, created = Token.objects.get_or_create(user=user)
        return token.key
