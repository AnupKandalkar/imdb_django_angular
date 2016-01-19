# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_moviesdata_moviepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesdata',
            name='popularity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='moviesdata',
            name='ssdb_score',
            field=models.IntegerField(),
        ),
    ]
