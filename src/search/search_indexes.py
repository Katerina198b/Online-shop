from __future__ import unicode_literals

from django.db import models

# Create your models here.

import datetime
from haystack import indexes
from product.models import Product

class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    created_at = indexes.DateTimeField(model_attr='created_at')

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created_at__lte=datetime.datetime.now())