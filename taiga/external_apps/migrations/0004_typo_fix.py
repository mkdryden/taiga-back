# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-05 20:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('external_apps', '0003_auto_20170607_2320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applicationtoken',
            options={'ordering': ['application', 'user'], 'verbose_name': 'application token', 'verbose_name_plural': 'application tokens'},
        ),
    ]
