# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shortcut',
            fields=[
                ('short', models.CharField(help_text='Name of the shortcut', max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('icon', models.CharField(blank=True, help_text='Path to an icon file', max_length=30)),
                ('template', models.CharField(help_text='http://example.com/?query={q} or search-in:http://example.com/', max_length=100)),
            ],
        ),
    ]
