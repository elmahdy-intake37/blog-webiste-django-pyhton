# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 19:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 10, 19, 24, 31, 713450)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 10, 19, 24, 31, 712624)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 10, 19, 24, 31, 714100)),
        ),
    ]
