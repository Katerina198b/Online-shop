from __future__ import unicode_literals
from django.db import models


class Core(models.Model):

    def __unicode__(self):
        return (self.title)
