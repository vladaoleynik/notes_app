# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_auto_20150621_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='media',
            field=models.FileField(null=True, upload_to=b'uploads/%Y/%m/%d/%H/%M/%S/', blank=True),
        ),
    ]
