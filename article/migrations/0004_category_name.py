# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_remove_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
