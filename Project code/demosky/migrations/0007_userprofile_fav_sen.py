# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demosky', '0006_merge_20171025_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='fav_sen',
            field=models.CharField(default=b'', max_length=10000),
        ),
    ]
