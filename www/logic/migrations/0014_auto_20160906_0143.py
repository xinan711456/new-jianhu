# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-06 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0013_mergemsg_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mergemsg',
            name='update_time',
            field=models.DateTimeField(),
        ),
    ]
