# Generated by Django 3.1.14 on 2022-03-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0030_auto_20220323_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='uuid',
            field=models.UUIDField(editable=False, verbose_name='Identifier', unique=True, blank=True),
        ),
    ]
