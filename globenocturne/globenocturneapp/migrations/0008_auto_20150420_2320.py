# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('globenocturneapp', '0007_auto_20150420_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldoriginalsol',
            name='sat',
            field=models.CharField(max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='worldoriginalsol',
            name='year',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
