# -*- coding: utf-8 -*-v

from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from adjacent import Client



class Product(models.Model):

    def __unicode__(self):
        return (self.name)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор')
    created_at = models.DateField(auto_now_add=True)
    changed_at = models.DateField(auto_now=True)
    name = models.CharField(max_length=255, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание')
    shop = models.ForeignKey('shop.Shop', default=1)
    publish = models.BooleanField(default=True, verbose_name='Опубликовать')
    image = models.ImageField(blank=True, null=True, verbose_name='Фотография')
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    category = models.ManyToManyField('Category', related_name='products')

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('product:about_product', args=[str(self.id)])

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
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Category(models.Model):

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    category = models.ManyToManyField('Product', related_name='categories')

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

'''
class Like(models.Model):

    def __unicode__(self):
        return (self.name)

    author = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like')
    product = models


@receiver(models.signals.post_save, sender=Comment)
def on_answer_creation(sender, instance, *args, **kwargs):
    client = Client()
    client.publish(instance.product.get_cent_answers_channel_name(), instance.as_compact_dict())
    response = client.send()
    print('sent to channel {}, got response from centrifugo: {}'.format(instance.question.get_cent_answers_channel_name(),
                                                                    response))
                                                                    '''
