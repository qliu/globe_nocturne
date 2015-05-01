# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('globenocturneapp', '0008_auto_20150420_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldoriginalsol',
            name='dn_range_max',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='worldoriginalsol',
            name='dn_range_min',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
