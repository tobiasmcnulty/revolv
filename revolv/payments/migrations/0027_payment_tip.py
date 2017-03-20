# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0026_auto_20170222_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='tip',
            field=models.ForeignKey(blank=True, to='payments.Tip', null=True),
            preserve_default=True,
        ),
    ]
