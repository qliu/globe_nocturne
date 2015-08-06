# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('globenocturneapp', '0016_auto_20150701_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldcountry',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
            preserve_default=True,
        ),
    ]
