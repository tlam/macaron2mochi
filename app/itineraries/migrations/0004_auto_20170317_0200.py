# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraries', '0003_auto_20170317_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]