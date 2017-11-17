# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_revolvuserprofile_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='revolvuserprofile',
            name='solar_seed_fund_pool',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='revolvuserprofile',
            name='subscribed_to_repayment_notifications',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
