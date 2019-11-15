# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0072_project_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cover_photo',
            field=imagekit.models.fields.ProcessedImageField(default=None, help_text=b'Choose a beautiful high resolution image to represent this project.', upload_to=b'covers/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='profile_picture',
            field=imagekit.models.fields.ProcessedImageField(default=b'/media/covers/genericprofile.jpg', upload_to=b'covers/', blank=True, help_text=b'Choose a beautiful high resolution profile image to represent this project.', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='subfund_payment',
            field=models.CharField(default=12, help_text=b'The id of the main project you are sub-fundraising for.', max_length=255),
            preserve_default=True,
        ),
    ]
