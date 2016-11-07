from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.

class WithLikeCount(models.Model):
    count = models.IntegerField()

class Likes(models.Model):
    def __unicode__(self):
        return (self.name)

    item_types = models.ForeignKey(ContentType)
    item_id = models.PositiveIntegerField()
    item = GenericForeignKey('item_types', 'item_id')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class Dislikes(models.Model):
    def __unicode__(self):
        return (self.name)

    item_types = models.ForeignKey(ContentType)
    item_id = models.PositiveIntegerField()
    item = GenericForeignKey('item_types', 'item_id')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)