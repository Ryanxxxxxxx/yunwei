# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-17 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0002_host_hostowner'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='host_name',
            field=models.CharField(default='', max_length=256, null=True, verbose_name='操作系统主机名'),
        ),
    ]