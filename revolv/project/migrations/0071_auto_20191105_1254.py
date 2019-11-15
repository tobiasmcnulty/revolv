# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0070_anonymoususerdonation'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='subfund_payment',
            field=models.CharField(default=12, help_text=b'How would you like to title this project?', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(help_text=b'This is the body of content that shows up on the project page.', null=True, verbose_name=b'Project description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='impact_power',
            field=models.FloatField(help_text=b'What is the expected output in killowatts of the proposed solar array?', null=True, verbose_name=b'Expected Killowatt Output', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='location',
            field=models.CharField(help_text=b'What is the address of the organization where the solar panels will be installed?', max_length=255, null=True, verbose_name=b'Organization Address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='location_latitude',
            field=models.DecimalField(default=0.0, null=True, max_digits=17, decimal_places=14, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='location_longitude',
            field=models.DecimalField(default=0.0, null=True, max_digits=17, decimal_places=14, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='mission_statement',
            field=models.TextField(help_text=b'What is the mission statement of the organization being helped by this project?', null=True, verbose_name=b'Organization Mission', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='org_about',
            field=models.TextField(help_text=b'Elaborate more about the organization, what it does, who it serves, etc.', null=True, verbose_name=b'Organization Description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='people_affected',
            field=models.PositiveIntegerField(default=0, help_text=b'How many people will be impacted by this project?', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='project_url',
            field=models.CharField(help_text=b'How to show project url for this project?', max_length=255, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='solar_url',
            field=models.URLField(help_text=b'This can be found by going to http://home.solarlog-web.net/, going to the             solar log profile for your site, and clicking on the Graphics sub-page. Copy and paste             the URL in the address bar into here.', max_length=255, null=True, verbose_name=b'Solar Log Graphics URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='tagline',
            field=models.CharField(help_text=b'Select a short tag line that describes this project. (No more than 100 characters.)', max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='total_kwh_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, blank=True, help_text=b'How much is the total kWH value for 25 years to this project?', null=True),
            preserve_default=True,
        ),
    ]
