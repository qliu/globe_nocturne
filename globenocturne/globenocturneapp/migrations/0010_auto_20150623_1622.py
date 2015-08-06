# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('globenocturneapp', '0009_auto_20150420_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worldcountry',
            name='area_km',
        ),
        migrations.AddField(
            model_name='worldcountry',
            name='capital',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='worldcountry',
            name='continent',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='worldcountry',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='worldcountry',
            name='name',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
    ]
