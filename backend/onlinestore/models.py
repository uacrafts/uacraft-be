from django.db import models


# Create your models here.
class CallBack(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
