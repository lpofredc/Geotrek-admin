# Generated by Django 3.2.25 on 2024-04-17 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trekking', '0048_auto_20230927_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trek',
            name='related_treks',
        ),
        migrations.DeleteModel(
            name='TrekRelationship',
        ),
    ]
