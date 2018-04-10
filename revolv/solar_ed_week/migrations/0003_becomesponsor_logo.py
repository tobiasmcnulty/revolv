# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solar_ed_week', '0002_becomepartner_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='becomesponsor',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'become_partner/', blank=True),
            preserve_default=True,
        ),
    ]
