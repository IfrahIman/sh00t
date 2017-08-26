# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 06:24
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0003_delete_templatemaster'),
    ]

    operations = [
        migrations.AddField(
            model_name='casemaster',
            name='description',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.AddField(
            model_name='casemaster',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='modulemaster',
            name='description',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.AddField(
            model_name='modulemaster',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
