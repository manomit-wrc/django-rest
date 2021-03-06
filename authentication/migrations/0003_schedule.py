# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-06-14 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_publish_publishasset'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('uid', models.CharField(max_length=150)),
                ('start_at', models.DateTimeField(auto_now_add=True)),
                ('is_loop', models.BooleanField(default=True)),
            ],
        ),
    ]
