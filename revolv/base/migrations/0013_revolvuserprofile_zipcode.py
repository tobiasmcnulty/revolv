# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_delete_newsletteruser'),
    ]

    operations = [
        migrations.AddField(
            model_name='revolvuserprofile',
            name='zipcode',
            field=models.CharField(default=b'', max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
    ]
