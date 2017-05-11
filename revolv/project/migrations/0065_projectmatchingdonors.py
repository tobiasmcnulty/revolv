# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_delete_newsletteruser'),
        ('project', '0064_project_project_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectMatchingDonors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('matching_donor', models.ForeignKey(related_name='matching_donor', to='base.RevolvUserProfile')),
                ('project', models.ForeignKey(to='project.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
