# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('i3', '0002_auto_20171118_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='multiplier',
            field=models.FloatField(default=0.01),
        ),
    ]