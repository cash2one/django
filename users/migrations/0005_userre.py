# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_delete_userre'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]