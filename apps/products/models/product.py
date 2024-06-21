from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Case
from django.db.models import When
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimestampMixin

MIN_QUANTITY_PRODUCTS = 0
ERROR_MIN_QUANTITY_PRODUCTS_MESSAGE = _(f'Must be greater than or equal to {MIN_QUANTITY_PRODUCTS}.')


class Product(TimestampMixin, models.Model):
    title = models.CharField(_('Назва продукту'), max_length=255)
    seller = models.ForeignKey(
        to='Seller',
        on_delete=models.CASCADE,
        related_name='product_sellers',
        verbose_name=_('Продавець')
    )
    price = models.OneToOneField(
        to='Price',
        on_delete=models.CASCADE,
        related_name='product',
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
        on_delete=models.PROTECT,
        related_name='category_products',
        verbose_name=_('Категорія'),
    )
    quantity_in_stock = models.PositiveIntegerField(
        _('Кількість товарів'),
        validators=[
            MinValueValidator(
                MIN_QUANTITY_PRODUCTS,
                message=_(ERROR_MIN_QUANTITY_PRODUCTS_MESSAGE)
            )
        ],
        default=MIN_QUANTITY_PRODUCTS
    )
    description = models.TextField(verbose_name=_('Опис товару'), blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product'
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукти')
        unique_together = ['title', 'seller']
        ordering = (
            Case(
                When(price__special_price__gt=0, then='price__special_price'),
                default='price__regular_price'
            ),
            'price__regular_price'
        )
