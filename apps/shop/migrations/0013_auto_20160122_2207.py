# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_user_dummy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dummy',
            field=models.TextField(max_length=2),
        ),
    ]
