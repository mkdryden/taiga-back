# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-14 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_user_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='accepted_terms',
            field=models.BooleanField(default=True, verbose_name='accepted terms'),
        ),
        migrations.AddField(
            model_name='user',
            name='read_new_terms',
            field=models.BooleanField(default=False, verbose_name='read new terms'),
        ),
    ]
