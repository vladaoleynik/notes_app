# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_color_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersettings',
            name='category',
            field=models.ManyToManyField(to='notes.Category', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='color',
            field=models.ManyToManyField(to='notes.Color', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='tag',
            field=models.ManyToManyField(to='notes.Tag', null=True, blank=True),
        ),
    ]
