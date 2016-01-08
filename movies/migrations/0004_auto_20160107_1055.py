# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_moviesdata_start'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviesdata',
            old_name='start',
            new_name='stars',
        ),
    ]
