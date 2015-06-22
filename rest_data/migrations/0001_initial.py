# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=40)),
                ('status', models.IntegerField(default=b'0')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(max_length=6)),
                ('status', models.IntegerField(default=b'0')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('text', models.TextField()),
                ('media', models.CharField(max_length=200, null=True, blank=True)),
                ('category', models.ForeignKey(to='rest_data.Category')),
                ('color', models.ForeignKey(to='rest_data.Color')),
            ],
            options={
                'permissions': (('view_notes', 'Anyone can see my notes'),),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=40)),
                ('status', models.IntegerField(default=b'0')),
            ],
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.ManyToManyField(to='rest_data.Category', blank=True)),
                ('color', models.ManyToManyField(to='rest_data.Color', blank=True)),
                ('tag', models.ManyToManyField(to='rest_data.Tag', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='tag',
            field=models.ManyToManyField(to='rest_data.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='note',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
