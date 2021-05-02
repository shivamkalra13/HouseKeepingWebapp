# Generated by Django 2.1.4 on 2019-07-14 16:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20190714_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='taskToBePerformedBy',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='timeOfAllocation',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]