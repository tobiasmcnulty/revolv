# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0068_stripedetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripedetails',
            name='donation_amount',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
