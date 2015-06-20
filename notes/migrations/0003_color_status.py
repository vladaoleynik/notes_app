# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20150620_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='status',
            field=models.CharField(default=b'user', max_length=10),
        ),
    ]
