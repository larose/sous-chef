# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-31 17:09
from __future__ import unicode_literals

import annoying.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0014_auto_20160826_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='client_id_sequence',
            field=annoying.fields.JSONField(blank=True, null=True),
        ),
    ]