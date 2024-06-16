from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimestampMixin


class Store(TimestampMixin, models.Model):
    class Status(models.IntegerChoices):
        DEACTIVATE = 0, _('Деактивовано')
        ACTIVE = 1, _('Активовано')

    title = models.CharField(_('Назва магазину'), max_length=255, unique=True, db_index=True)
    city = models.CharField(_('Місто'), max_length=255)
    is_displayed = models.BooleanField(
        choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
        db_index=True,
        default=Status.ACTIVE,
        verbose_name=_('Статус')
    )

    def __str__(self):
        return f'{self.title} | {self.city}'

    class Meta:
        db_table = 'product_store'
        verbose_name = _('Магазин')
        verbose_name_plural = _('Магазини')
