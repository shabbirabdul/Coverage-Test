# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='subscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=50, verbose_name=b'Email Address')),
                ('fname', models.CharField(max_length=25, verbose_name=b'First Name', blank=True)),
                ('lname', models.CharField(max_length=25, verbose_name=b'Last Name', blank=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Subscribers',
            },
            bases=(models.Model,),
        ),
    ]
