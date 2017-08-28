# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_delete_newsletteruser'),
        ('project', '0065_projectmatchingdonors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='ambassador',
        ),
        migrations.AddField(
            model_name='project',
            name='ambassadors',
            field=models.ManyToManyField(related_name='ambassadors', null=True, to='base.RevolvUserProfile'),
            preserve_default=True,
        ),
    ]
