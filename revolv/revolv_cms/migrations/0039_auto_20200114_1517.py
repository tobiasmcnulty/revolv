# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revolv_cms', '0038_auto_20190801_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpagesettings',
            name='how_it_works_intro',
            field=models.TextField(default=b"We believe that everyone should have the ability to support clean energy. So we created a new way for people to take action. It's a pretty simple idea. We raise money through crowdsource funding to put solar panels on community-serving nonprofit organizations and worker-owned cooperatives. As these organizations pay us back, we reinvest the money into more solar projects in communities across the country. This creates a revolving fund for solar energy that continually perpetuates itself building more and more solar. It's a pay-it-forward model for community solar. We call it the Solar Seed Fund.", help_text=b"Intro paragraph for the 'Learn about how RE-volv works' section of the homepage."),
            preserve_default=True,
        ),
    ]
