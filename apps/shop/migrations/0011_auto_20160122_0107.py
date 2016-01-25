# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 01:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('shop', '0010_auto_20160121_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='procItems',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('products.items',),
        ),
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Items'),
        ),
    ]