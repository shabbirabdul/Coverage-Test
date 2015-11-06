# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='range',
            field=models.IntegerField(default=b'0'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subscriber',
            name='sector',
            field=models.CharField(default=b'-', max_length=2, verbose_name=b'Sector', choices=[(b'AG', b'Agriculture'), (b'FR', b'Forestry'), (b'-', b'All')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=b'Email Address'),
            preserve_default=True,
        ),
    ]
