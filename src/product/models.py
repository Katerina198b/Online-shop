# -*- coding: utf-8 -*-v

from __future__ import unicode_literals
from django.db import models


class Product(models.Model):

    def __unicode__(self):
        return (self.name)

    created_at = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255, verbose_name='Название товара', default= 'Название товара')
    description = models.TextField(verbose_name='Описание', default='Описание')
    changed_at = models.DateField(auto_now=True)
    shop = models.ForeignKey('shop.Shop', default=1)
    publish = models.BooleanField(default=True)
    # КАРТИНКИ И ФАЙЛЫ
    image = models.ImageField(default='product.jpg')
    #file = models.FileField()

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
