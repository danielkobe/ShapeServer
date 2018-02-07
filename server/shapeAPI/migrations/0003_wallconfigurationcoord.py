# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 02:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shapeAPI', '0002_wallconfiguration_timechanged'),
    ]

    operations = [
        migrations.CreateModel(
            name='WallConfigurationCoord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('w', models.IntegerField()),
                ('h', models.IntegerField()),
                ('timeChangedCoor', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
