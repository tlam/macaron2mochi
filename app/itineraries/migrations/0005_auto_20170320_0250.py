# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 02:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itineraries', '0004_auto_20170317_0200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itinerary',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itineraries', to='trips.Trip'),
        ),
    ]
