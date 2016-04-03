# -*- coding: utf-8 -*-v

from __future__ import unicode_literals
from django.db import models


class Comment(models.Model):

    def __unicode__(self):
        return ('Комментарий #{num}'.format(num=self.id))

    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    post = models.ForeignKey('product.Product')
    pub_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
