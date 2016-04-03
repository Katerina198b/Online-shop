from __future__ import unicode_literals
from django.db import models
from django.views.generic import CreateView
from django.contrib.auth import get_user_model


class Core(models.Model):

    def __unicode__(self):
        return (self.title)


#class CreateUser(CreateView):
#    model=get_user_model()