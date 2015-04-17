# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('globenocturneapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DMSPDataset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('wms_layer', models.CharField(max_length=100, verbose_name=b'WMS Layer')),
            ],
            options={
                'db_table': 'dmsp_dataset',
                'verbose_name': 'DMSP Dataset',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DMSPProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'dmsp_product',
                'verbose_name': 'DMSP Product',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Satellite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'satellite',
                'verbose_name': 'Satellite',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SatYear',
            fields=[
                ('year', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'sat_year',
                'verbose_name': 'Year',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dmspdataset',
            name='product',
            field=models.ForeignKey(verbose_name=b'DMSP Product', to='globenocturneapp.DMSPProduct'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dmspdataset',
            name='satellite',
            field=models.ForeignKey(verbose_name=b'Satellite', to='globenocturneapp.Satellite'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dmspdataset',
            name='year',
            field=models.ForeignKey(verbose_name=b'Year', to='globenocturneapp.SatYear'),
            preserve_default=True,
        ),
    ]
