# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20150620_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersettings',
            name='category',
            field=models.ManyToManyField(to='notes.Category', blank=True),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='color',
            field=models.ManyToManyField(to='notes.Color', blank=True),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='tag',
            field=models.ManyToManyField(to='notes.Tag', blank=True),
        ),
    ]
