from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductImage(models.Model):
    product = models.ForeignKey(
        to='Product',
        on_delete=models.CASCADE,
        related_name='prod_images'
    )
    image = models.ImageField(_('Фото'), upload_to='products/')

    def __str__(self):
        return f"Фото для продукта '{self.product.title}'"

    class Meta:
        db_table = 'product_image'
        verbose_name = _('Фото продукта')
        verbose_name_plural = _('Фото продуктів')
