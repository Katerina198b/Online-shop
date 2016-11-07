# -*- coding: utf-8 -*-v

from __future__ import unicode_literals
from django.db import models


class Review(models.Model):
    text = models.TextField(verbose_name="Отзыв")

