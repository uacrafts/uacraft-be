from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimestampMixin

NO_BRAND = 'Без бренду'


class Brand(TimestampMixin, models.Model):
    title = models.CharField(
        verbose_name=_('Назва бренду'),
        max_length=100,
        unique=True,
        default=NO_BRAND
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product_brand'
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренди'
        ordering = ('title',)
