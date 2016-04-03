# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.conf import settings #предзаполняет settngs дефолными значениями

class Shop(models.Model):

    def __unicode__(self):
        return (self.name)

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    owner = models.CharField(max_length=255, verbose_name='Владелец', default='Владелец')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')  # время создания
    name = models.CharField(max_length=255, verbose_name='Заголовок', default='Название магазина')
    description = models.TextField(verbose_name='Краткое описание', default='Краткое описание')

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"
        ordering = ('created_at', )


