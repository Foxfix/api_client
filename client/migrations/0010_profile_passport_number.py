# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-17 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_auto_20170417_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='passport_number',
            field=models.CharField(default='BC123456', max_length=15),
        ),
    ]
