# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_auto_20150622_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='media',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
