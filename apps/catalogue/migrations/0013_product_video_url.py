# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-15 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0012_auto_20170609_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='video_url',
            field=models.URLField(blank=True),
        ),
    ]
