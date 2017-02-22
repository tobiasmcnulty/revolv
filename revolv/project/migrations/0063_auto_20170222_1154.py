# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0062_auto_20160212_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='total_kwh_value',
            field=models.DecimalField(default=0, help_text=b'How much is the total kWH value for 25 years to this project?', max_digits=15, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='solar_url',
            field=models.URLField(help_text=b'This can be found by going to http://home.solarlog-web.net/, going to the             solar log profile for your site, and clicking on the Graphics sub-page. Copy and paste             the URL in the address bar into here.', max_length=255, verbose_name=b'Solar Log Graphics URL', blank=True),
            preserve_default=True,
        ),
    ]
