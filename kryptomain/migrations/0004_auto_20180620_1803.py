# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-06-20 16:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kryptomain', '0003_auto_20180620_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tematycznypost',
            name='data_wpisu',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 20, 18, 3, 37, 332884), verbose_name='data wpisu'),
        ),
    ]