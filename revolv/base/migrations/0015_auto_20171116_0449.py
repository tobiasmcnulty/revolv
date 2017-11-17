# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20171110_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revolvuserprofile',
            name='subscribed_to_updates',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
