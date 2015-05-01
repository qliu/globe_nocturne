# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('globenocturneapp', '0004_auto_20150420_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='worldcountry',
            name='fips',
            field=models.CharField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='worldcountry',
            name='iso',
            field=models.CharField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='worldcountry',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
