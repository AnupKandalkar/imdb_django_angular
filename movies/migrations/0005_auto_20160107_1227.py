# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20160107_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesdata',
            name='create_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
