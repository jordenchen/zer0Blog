# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-13 02:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='editor_choice',
            field=models.ForeignKey(blank=True, default='tinyMCE', null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Editor'),
        ),
    ]
