# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BecomePartner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('organization', models.CharField(max_length=255)),
                ('promote_solar', models.BooleanField(default=False)),
                ('promoting_way', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BecomeSponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('organization', models.CharField(max_length=255)),
                ('financially_support', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HostEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255, null=True, blank=True)),
                ('state', models.CharField(max_length=255, null=True, blank=True)),
                ('zip_code', models.CharField(max_length=255, null=True, blank=True)),
                ('detail', models.TextField()),
                ('facebook_link', models.CharField(max_length=255, null=True, blank=True)),
                ('latitude', models.DecimalField(default=0.0, max_digits=17, decimal_places=14)),
                ('longitude', models.DecimalField(default=0.0, max_digits=17, decimal_places=14)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
