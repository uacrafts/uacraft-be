from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

MIN_PRICE = 0.0
ERROR_MIN_PRICE_MESSAGE = f'Must be greater than or equal to {MIN_PRICE}.'


class Price(models.Model):
    regular_price = models.DecimalField(
        _('Звичайна ціна'),
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(
                MIN_PRICE, message=_(ERROR_MIN_PRICE_MESSAGE)
            )
        ]
    )
    special_price = models.DecimalField(
        _('Ціна зі знижкою'),
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(
                MIN_PRICE, message=_(ERROR_MIN_PRICE_MESSAGE)
            )
        ],
        default=MIN_PRICE
    )
    discount_percentage = models.DecimalField(
        _('Відсоток знижки'),
        max_digits=10,
        decimal_places=1,
        default=MIN_PRICE
    )

    def __str__(self):
        return f"{self.special_price or self.regular_price}"

    def clean(self):
        if self.special_price > self.regular_price:
            raise ValidationError(_('Ціна зі знижкою не може перевищувати звичайну ціну.'))
        super().clean()

    def save(self, *args, **kwargs):
        if self.special_price > 0:
            self.discount_percentage = ((self.regular_price - self.special_price) / self.regular_price) * 100
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'product_price'
        verbose_name = _('Ціна')
        verbose_name_plural = _('Ціни')
