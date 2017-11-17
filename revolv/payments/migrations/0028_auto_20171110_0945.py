# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20171110_0945'),
        ('project', '0069_stripedetails_donation_amount'),
        ('payments', '0027_payment_tip'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolarSeedFund',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(to='project.Project')),
                ('user', models.ForeignKey(to='base.RevolvUserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='payment',
            name='solar_seed_monthly',
            field=models.ForeignKey(blank=True, to='payments.SolarSeedFund', null=True),
            preserve_default=True,
        ),
    ]
