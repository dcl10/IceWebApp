# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_auto_20170927_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='DOB',
            field=models.CharField(max_length=15),
        ),
    ]
