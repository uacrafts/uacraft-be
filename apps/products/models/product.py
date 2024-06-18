from django.db import models
from django.db.models import Case
from django.db.models import When
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimestampMixin


class Product(TimestampMixin, models.Model):
    title = models.CharField(_('Назва продукту'), max_length=255)
    store = models.ForeignKey(
        to='Store',
        on_delete=models.SET_NULL,
        null=True,
        related_name='product_stores',
        verbose_name=_('Назва магазину')
    )
    price = models.ForeignKey(
        to='Price',
        on_delete=models.SET_NULL,
        null=True,
        related_name='product_prices',
        verbose_name=_('Ціна'),
    )
    brand = models.ForeignKey(
        to='Brand',
        on_delete=models.SET_NULL,
        null=True,
        related_name='brand_products',
        verbose_name=_('Назва бренду'),
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='category_products',
        verbose_name=_('Категорії'),
    )
    images = models.ManyToManyField(
        to='ProductImage',
        related_name='product_images',
        blank=True,
        verbose_name=_('Фото товару'),
    )
    description = models.TextField(verbose_name=_('Опис товару'), blank=True)
    is_stock = models.BooleanField(_('Наявність'))

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product'
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукти')
        unique_together = ['title', 'store']
        ordering = (
            Case(
                When(price__special_price__gt=0, then='price__special_price'),
                default='price__regular_price'
            ),
            'price__regular_price'
        )
