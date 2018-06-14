# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-06-14 20:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 6, 14, 20, 44, 46, 840853, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='date_schedule',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2018, 6, 14, 20, 45, 0, 313891, tzinfo=utc)),
            preserve_default=False,
        ),
    ]