# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 11:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170322_1643'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserRe',
        ),
    ]
