# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0071_auto_20191105_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='profile_picture',
            field=imagekit.models.fields.ProcessedImageField(default=None, upload_to=b'covers/', blank=True, help_text=b'Choose a beautiful high resolution profile image to represent this project.', null=True),
            preserve_default=True,
        ),
    ]
