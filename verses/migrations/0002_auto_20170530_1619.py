# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('verses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verse',
            name='awana_book',
            field=models.CharField(max_length=5, choices=[('C-HON', 'Cubbies Honeycomb'), ('C-APP', 'Cubbies Appleseed')]),
        ),
        migrations.AlterField(
            model_name='verse',
            name='bible_chapter',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='verse',
            name='bible_verse',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
