# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_auto_20170912_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='id',
        ),
        migrations.AlterField(
            model_name='patient',
            name='nhs_number',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]