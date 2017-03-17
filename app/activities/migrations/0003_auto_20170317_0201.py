# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20170317_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=10),
        ),
    ]
