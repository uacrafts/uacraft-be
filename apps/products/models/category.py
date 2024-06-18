from django.db import models
from django.utils.translation import gettext_lazy as _
from slugify import slugify
from unidecode import unidecode

from apps.common.models import TimestampMixin


class Category(TimestampMixin, models.Model):
    title = models.CharField(_('Назва категорії'), max_length=100)

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_('Батьківська категорія')
    )
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(unidecode(self.title))
        return super().save(*args, **kwargs)

    class Meta:
        db_table = 'product_category'
        verbose_name = _('Категорія')
        verbose_name_plural = _('Категорії')
        ordering = ('title',)
