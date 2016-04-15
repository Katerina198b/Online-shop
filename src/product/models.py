# -*- coding: utf-8 -*-v

from __future__ import unicode_literals
from django.db import models
from django.conf import settings

class Product(models.Model):

    def __unicode__(self):
        return (self.name)

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание')
    changed_at = models.DateField(auto_now=True)
    shop = models.ForeignKey('shop.Shop', default=1)
    publish = models.BooleanField(default=True, verbose_name='Опубликовать')
    # КАРТИНКИ И ФАЙЛЫ
    image = models.ImageField(blank=True, null=True, verbose_name='Фотография')
    #file = models.FileField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class Comment(models.Model):

    def __unicode__(self):
        return ('Комментарий #{num}'.format(num=self.id))

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name="Комментарий")
    product = models.ForeignKey('Product', related_name='comments')
    pub_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
