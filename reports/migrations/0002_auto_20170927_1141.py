# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]