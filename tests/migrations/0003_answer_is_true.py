# Generated by Django 2.0 on 2017-12-12 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_auto_20171212_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='is_true',
            field=models.BooleanField(default=False),
        ),
    ]
