# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorldBorder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iso', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=50)),
                ('countryaff', models.CharField(max_length=50)),
                ('affiso', models.CharField(max_length=2)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=3857)),
            ],
            options={
                'db_table': 'worldborder',
                'verbose_name': 'World Border',
            },
            bases=(models.Model,),
        ),
    ]
