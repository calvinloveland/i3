# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('i3', '0006_auto_20171118_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='shield_instability',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ship',
            name='current_shield',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ship',
            name='ideal_shield',
            field=models.IntegerField(default=0),
        ),
    ]
