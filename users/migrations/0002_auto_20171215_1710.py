# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-15 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='finishtest',
            name='count_false_answer',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='finishtest',
            name='count_true_answer',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
