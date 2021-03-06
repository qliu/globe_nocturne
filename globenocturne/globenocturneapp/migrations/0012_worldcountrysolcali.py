# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('globenocturneapp', '0011_worldcountrysol'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorldCountrySOLCali',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(null=True, blank=True)),
                ('sat', models.CharField(max_length=3)),
                ('sol', models.IntegerField(null=True, blank=True)),
                ('pixel_count', models.IntegerField(null=True, blank=True)),
                ('dn_mean', models.FloatField(null=True, blank=True)),
                ('dn_stddev', models.FloatField(null=True, blank=True)),
                ('dn_min', models.IntegerField(null=True, blank=True)),
                ('dn_max', models.IntegerField(null=True, blank=True)),
                ('country', models.ForeignKey(to='globenocturneapp.WorldCountry')),
            ],
            options={
                'db_table': 'world_country_sol_cali',
                'verbose_name': 'World Country Sum of Light After Intercalibrated',
            },
            bases=(models.Model,),
        ),
    ]
