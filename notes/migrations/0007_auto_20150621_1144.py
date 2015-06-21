# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20150621_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.IntegerField(default=b'0'),
        ),
        migrations.AlterField(
            model_name='color',
            name='status',
            field=models.IntegerField(default=b'0'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='status',
            field=models.IntegerField(default=b'0'),
        ),
    ]
