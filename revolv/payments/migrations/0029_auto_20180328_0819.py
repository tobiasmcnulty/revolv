# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0028_auto_20171110_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferralSourceTrack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.CharField(max_length=255, null=True, blank=True)),
                ('medium', models.CharField(max_length=255, null=True, blank=True)),
                ('campaign', models.CharField(max_length=255, null=True, blank=True)),
                ('content', models.CharField(max_length=255, null=True, blank=True)),
                ('payment', models.ForeignKey(to='payments.Payment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='projectmontlyrepaymentconfig',
            name='year',
            field=models.PositiveSmallIntegerField(default=2018),
            preserve_default=True,
        ),
    ]
