# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('globenocturneapp', '0015_auto_20150701_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldcountry',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
