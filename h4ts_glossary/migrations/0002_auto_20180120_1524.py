# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 15:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('h4ts_glossary', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='glossary_term',
            new_name='GlossaryTerm',
        ),
    ]