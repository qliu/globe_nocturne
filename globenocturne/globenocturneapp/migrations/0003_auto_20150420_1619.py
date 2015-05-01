# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('globenocturneapp', '0002_auto_20150416_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorldCountry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fips', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=200)),
                ('area_km', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'world_countries',
                'verbose_name': 'World Country',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorldGDP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(null=True, blank=True)),
                ('value', models.FloatField(null=True, blank=True)),
                ('country', models.ForeignKey(to='globenocturneapp.WorldCountry')),
            ],
            options={
                'db_table': 'world_gdp',
                'verbose_name': 'World GDP',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorldOriginalSOM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('som', models.FloatField(null=True, blank=True)),
                ('dn_range_min', models.IntegerField(null=True, blank=True)),
                ('dn_range_max', models.IntegerField(null=True, blank=True)),
                ('pixels_in_polygon', models.IntegerField(null=True, blank=True)),
                ('pixels_in_range', models.IntegerField(null=True, blank=True)),
                ('pixels_zero', models.IntegerField(null=True, blank=True)),
                ('dn_min', models.FloatField(null=True, blank=True)),
                ('dn_max', models.FloatField(null=True, blank=True)),
                ('avg', models.FloatField(null=True, blank=True)),
                ('country', models.ForeignKey(to='globenocturneapp.WorldCountry')),
                ('sat', models.ForeignKey(verbose_name=b'Satellite', to='globenocturneapp.Satellite')),
                ('year', models.ForeignKey(verbose_name=b'Year', to='globenocturneapp.SatYear')),
            ],
            options={
                'db_table': 'world_original_som',
                'verbose_name': 'World Original SOM',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorldPoulation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(null=True, blank=True)),
                ('value', models.FloatField(null=True, blank=True)),
                ('country', models.ForeignKey(to='globenocturneapp.WorldCountry')),
            ],
            options={
                'db_table': 'world_population',
                'verbose_name': 'World Poulation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorldSOM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(null=True, blank=True)),
                ('value', models.FloatField(null=True, blank=True)),
                ('country', models.ForeignKey(to='globenocturneapp.WorldCountry')),
            ],
            options={
                'db_table': 'world_som',
                'verbose_name': 'World SOM',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='dmspdataset',
            name='name',
            field=models.CharField(max_length=100, null=b'True', blank=b'True'),
            preserve_default=True,
        ),
    ]
