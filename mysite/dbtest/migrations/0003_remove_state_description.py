# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-27 01:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbtest', '0002_remove_user_process_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='description',
        ),
    ]
