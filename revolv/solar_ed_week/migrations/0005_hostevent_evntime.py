# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solar_ed_week', '0004_auto_20180410_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostevent',
            name='evntime',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
    ]
