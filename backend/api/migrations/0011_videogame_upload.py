# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-15 04:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_videogame_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='videogame',
            name='upload',
            field=models.ImageField(default='some_string', upload_to='uploads/'),
        ),
    ]