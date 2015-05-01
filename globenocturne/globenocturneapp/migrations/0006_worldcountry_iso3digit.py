# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('globenocturneapp', '0005_auto_20150420_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='worldcountry',
            name='iso3digit',
            field=models.CharField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
    ]
