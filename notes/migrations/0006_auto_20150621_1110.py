# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20150620_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.CharField(default=b'user', max_length=10),
        ),
        migrations.AddField(
            model_name='tag',
            name='status',
            field=models.CharField(default=b'user', max_length=10),
        ),
    ]
