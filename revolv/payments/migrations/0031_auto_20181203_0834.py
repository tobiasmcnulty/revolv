# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0030_auto_20181009_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmontlyrepaymentconfig',
            name='starting_month',
            field=models.CharField(default=b'December', max_length=25),
            preserve_default=True,
        ),
    ]
