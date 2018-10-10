# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0031_auto_20180921_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmontlyrepaymentconfig',
            name='month',
            field=models.CharField(default=b'October', max_length=25),
            preserve_default=True,
        ),
    ]
