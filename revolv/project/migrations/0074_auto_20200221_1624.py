# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0073_auto_20191106_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='carbon_avoided',
            field=models.CharField(help_text=b'CO2 avoided for this project - new field', max_length=255, null=True, verbose_name=b'CO2 Avoided', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='dollars_saved',
            field=models.CharField(help_text=b'Lifetime electricity savings for this project - new field', max_length=255, null=True, verbose_name=b'Dollars Saved', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='financial_product',
            field=models.CharField(help_text=b'The type of financial product ( PPA or LEASE ) - new fields', max_length=255, null=True, verbose_name=b'Financial product', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='installation_date_status',
            field=models.CharField(help_text=b'Date of installation for this project - new fields', max_length=255, null=True, verbose_name=b'Installation Date Status', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='installation_status',
            field=models.CharField(help_text=b'Status of installation for this project - new field', max_length=255, null=True, verbose_name=b'Installation Status', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='cover_photo',
            field=imagekit.models.fields.ProcessedImageField(default=None, help_text=b'Choose a beautiful high resolution image to represent this project.', upload_to=b'covers/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='video_url',
            field=models.URLField(help_text=b'Link to a Youtube video about the project or community.', max_length=255, null=True, verbose_name=b'Video URL', blank=True),
            preserve_default=True,
        ),
    ]
