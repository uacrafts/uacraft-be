from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(label=_('Email'), write_only=True, required=True)
    password = serializers.CharField(
        label=_('Password'),
        style={'input_type': 'password'},
        write_only=True,
        required=True
    )

    def validate(self, attrs):
        user = authenticate(
            request=self.context.get('request'),
            username=attrs.get('email'),
            password=attrs.get('password')
        )
        if not user:
            raise serializers.ValidationError(
                _('User not found or credentials are not valid.'),
                code='authorization',
            )

        access_token, created = Token.objects.get_or_create(user=user)

        return {
            'access_token': access_token.key,
            'is_email_verified': user.is_email_verified,
        }


class LoginResponseSerializer(serializers.Serializer):
    is_email_verified = serializers.BooleanField()
    access_token = serializers.CharField()
