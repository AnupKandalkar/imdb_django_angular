# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoviesData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, null=True, blank=True)),
                ('director', models.CharField(max_length=40, null=True, blank=True)),
                ('ssdb_score', models.FloatField()),
                ('popularity', models.FloatField()),
                ('create_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MoviesGenre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre', models.CharField(max_length=40, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='moviesdata',
            name='genre',
            field=models.ManyToManyField(to='movies.MoviesGenre'),
        ),
    ]
