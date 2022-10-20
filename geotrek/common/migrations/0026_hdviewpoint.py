# Generated by Django 3.2.15 on 2022-10-20 15:07

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('common', '0025_auto_20220425_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='HDViewPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_insert', models.DateTimeField(auto_now_add=True, verbose_name='Insertion date')),
                ('date_update', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Update date')),
                ('picture', models.FileField(upload_to='', verbose_name='Picture')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=2154, verbose_name='Location')),
                ('object_id', models.PositiveIntegerField()),
                ('annotations', models.JSONField(blank=True, null=True, verbose_name='Annotations')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('author', models.CharField(blank=True, default='', help_text='Original creator', max_length=128, verbose_name='Author')),
                ('title', models.CharField(help_text='Title for this view point', max_length=1024, verbose_name='Title')),
                ('legend', models.CharField(blank=True, default='', help_text='Details about this view', max_length=1024, verbose_name='Legend')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('license', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.license', verbose_name='License')),
            ],
            options={
                'verbose_name': 'HD View',
                'verbose_name_plural': 'HD Views',
            },
        ),
    ]
