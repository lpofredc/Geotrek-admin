# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-12-19 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0005_baseinfrastructure_eid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseinfrastructure',
            name='eid',
            field=models.CharField(blank=True, db_column=b'id_externe', max_length=1024, null=True, verbose_name='External id'),
        ),
    ]
