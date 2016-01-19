# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20160119_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesdata',
            name='popularity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='moviesdata',
            name='ssdb_score',
            field=models.IntegerField(default=0),
        ),
    ]
