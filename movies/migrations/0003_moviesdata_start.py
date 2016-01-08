# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviesdata_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviesdata',
            name='start',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
    ]
