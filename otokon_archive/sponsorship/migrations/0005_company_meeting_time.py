# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-27 14:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sponsorship', '0004_organization_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='meeting_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 27, 14, 54, 36, 448328, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
