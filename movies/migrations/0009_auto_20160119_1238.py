# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_auto_20160119_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesdata',
            name='genre',
            field=models.ManyToManyField(related_name='moviegenre', to='movies.MoviesGenre'),
        ),
    ]
