# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('globenocturneapp', '0003_auto_20150420_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorldOriginalSOL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sol', models.FloatField(null=True, blank=True)),
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
                'db_table': 'world_original_sol',
                'verbose_name': 'World Original Sum of Lights Records',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorldSOL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(null=True, blank=True)),
                ('value', models.FloatField(null=True, blank=True)),
                ('country', models.ForeignKey(to='globenocturneapp.WorldCountry')),
            ],
            options={
                'db_table': 'world_sol',
                'verbose_name': 'World Sum of Lights',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='worldoriginalsom',
            name='country',
        ),
        migrations.RemoveField(
            model_name='worldoriginalsom',
            name='sat',
        ),
        migrations.RemoveField(
            model_name='worldoriginalsom',
            name='year',
        ),
        migrations.DeleteModel(
            name='WorldOriginalSOM',
        ),
        migrations.RemoveField(
            model_name='worldsom',
            name='country',
        ),
        migrations.DeleteModel(
            name='WorldSOM',
        ),
        migrations.RenameField(
            model_name='worldcountry',
            old_name='fips',
            new_name='iso',
        ),
    ]
