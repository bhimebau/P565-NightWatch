# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demosky', '0010_auto_20171125_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='token_valid',
            field=models.BooleanField(default=False),
        ),
    ]