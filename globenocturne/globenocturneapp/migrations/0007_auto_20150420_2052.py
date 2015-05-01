# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('globenocturneapp', '0006_worldcountry_iso3digit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldcountry',
            name='iso3digit',
            field=models.CharField(max_length=3, null=True, blank=True),
            preserve_default=True,
        ),
    ]
