# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 10:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20160417_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]