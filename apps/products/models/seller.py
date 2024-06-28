from django.db import models
from django.utils.translation import gettext_lazy as _
from slugify import slugify
from unidecode import unidecode

from apps.common.models import TimestampMixin


class Seller(TimestampMixin, models.Model):
    class Status(models.IntegerChoices):
        DEACTIVATE = 0, _('Деактивовано')
        ACTIVE = 1, _('Активовано')

    title = models.CharField(_('Назва продавця'), max_length=255)
    city = models.CharField(_('Місто'), max_length=255)
    is_displayed = models.BooleanField(
        choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
        db_index=True,
        default=Status.ACTIVE,
        verbose_name=_('Статус')
    )
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.title} | {self.city}'

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'product_seller'
        verbose_name = _('Продавець')
        verbose_name_plural = _('Продавці')
