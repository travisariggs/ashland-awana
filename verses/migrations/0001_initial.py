# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recitation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('result', models.CharField(choices=[('F', 'Failed'), ('H', 'Success with help'), ('S', 'Success')], default='F', max_length=1)),
                ('recited_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, blank=True)),
                ('birthday', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Verse',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('bible_book', models.CharField(max_length=30, blank=True)),
                ('bible_chapter', models.IntegerField(blank=True)),
                ('bible_verse', models.IntegerField(blank=True)),
                ('awana_book', models.CharField(choices=[('HON', 'HONEYCOMB'), ('APP', 'APPLESEED')], max_length=5)),
                ('awana_verse', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='recitation',
            name='student',
            field=models.ForeignKey(to='verses.Student'),
        ),
        migrations.AddField(
            model_name='recitation',
            name='verse',
            field=models.ForeignKey(to='verses.Verse'),
        ),
    ]
