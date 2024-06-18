from django.db import models
from django.utils.translation import gettext_lazy as _


class Price(models.Model):
    regular_price = models.DecimalField(_('Звичайна ціна'), max_digits=10, decimal_places=2)
    special_price = models.DecimalField(_('Ціна зі знижкою'), max_digits=10, decimal_places=2, default=0)
    discount_percentage = models.DecimalField(_('Відсоток знижки'), max_digits=10, decimal_places=1, default=0)

    def __str__(self):
        return f"{self.special_price or self.regular_price}"

    def save(self, *args, **kwargs):
        if self.special_price > 0:
            self.discount_percentage = ((self.regular_price - self.special_price) / self.regular_price) * 100
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'product_price'
        verbose_name = _('Ціна')
        verbose_name_plural = _('Ціни')
