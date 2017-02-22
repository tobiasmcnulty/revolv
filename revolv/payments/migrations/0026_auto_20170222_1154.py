# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0025_auto_20160210_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmontlyrepaymentconfig',
            name='year',
            field=models.PositiveSmallIntegerField(default=2017),
            preserve_default=True,
        ),
    ]
