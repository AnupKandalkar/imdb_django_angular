# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20160107_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviesdata',
            name='moviepic',
            field=models.ImageField(null=True, upload_to=b'%Y/%m/%d', blank=True),
        ),
    ]
