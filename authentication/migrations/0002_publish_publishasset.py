# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-06-14 18:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('uid', models.CharField(max_length=150)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_completed', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PublishAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('uid', models.CharField(max_length=150)),
                ('url', models.CharField(max_length=255)),
                ('type_of_assets', models.CharField(default='TVSHOW', max_length=50)),
                ('publish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Publish')),
            ],
        ),
    ]
