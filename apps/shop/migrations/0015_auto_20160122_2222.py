# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 22:22
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20160122_2208'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='cart',
            managers=[
                ('objectsM', django.db.models.manager.Manager()),
            ],
        ),
    ]