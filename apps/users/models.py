from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.users.managers import UserManager


class User(PermissionsMixin, AbstractBaseUser):
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _('A user with that username already exists.'),
        },
    )
    email = models.EmailField(_('email address'), unique=True)
    is_email_verified = models.BooleanField(
        _('email підтверджений'),
        default=False,
        help_text=_('Вказує, чи підтвердив користувач свою електронну адресу.')
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    class Meta:
        verbose_name = _('Користувача')
        verbose_name_plural = _('Користувачі')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
