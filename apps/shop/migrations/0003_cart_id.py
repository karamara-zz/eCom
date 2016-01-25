# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20160121_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='id',
            field=models.AutoField(default=1, primary_key=True),
            preserve_default=False,
        ),
    ]
