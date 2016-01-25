# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.IntegerField()),
                ('productName', models.TextField(max_length=45)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=45)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('qty', models.IntegerField()),
                ('user', models.OneToOneField(primary_key=True, serialize=False, to='shop.User')),
                ('products', models.ManyToManyField(to='shop.Product')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]
