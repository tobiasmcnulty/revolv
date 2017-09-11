# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_revolvuserprofile_zipcode'),
        ('project', '0067_anonymoususerdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='StripeDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stripe_customer_id', models.CharField(max_length=32, null=True, blank=True)),
                ('subscription_id', models.CharField(max_length=32, null=True, blank=True)),
                ('plan', models.CharField(max_length=64, null=True, blank=True)),
                ('stripe_email', models.EmailField(default=b'', max_length=75)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('amount', models.FloatField(default=0)),
                ('user', models.ForeignKey(related_name='stripe_donor', to='base.RevolvUserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
