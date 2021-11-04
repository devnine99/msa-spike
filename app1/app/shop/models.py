from django.db import models


class Shop(models.Model):
    name = models.CharField(verbose_name='이름', max_length=16)
    description = models.CharField(verbose_name='설명', max_length=128)

    class Meta:
        verbose_name = '샵'
        verbose_name_plural = verbose_name
