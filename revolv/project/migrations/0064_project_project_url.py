# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0063_auto_20170222_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_url',
            field=models.CharField(help_text=b'How to show project url for this project?', max_length=255, null=True),
            preserve_default=True,
        ),
    ]
