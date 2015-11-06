# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0003_auto_20150408_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='sector',
            field=models.CharField(default=b'-', max_length=2, verbose_name=b'Sector', choices=[(b'AG', b'Agriculture'), (b'FR', b'Forestry'), (b'-', b'All')]),
            preserve_default=True,
        ),
    ]
