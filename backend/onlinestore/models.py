from django.db import models
from django.utils import timezone


# Create your models here.
class CallBack(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)

    def delete(self, *args, **kwargs):
        if timezone.now() - self.created_at > timezone.timedelta(days=1):
            super().delete(*args, **kwargs)
