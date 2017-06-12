# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 16:58
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.CharField(max_length=100, verbose_name='\u67e5\u8be2\u8bb0\u5f55')),
                ('time', models.DateField(default=datetime.datetime.now, verbose_name='\u67e5\u8be2\u65f6\u95f4')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u67e5\u8be2\u4eba')),
            ],
        ),
    ]