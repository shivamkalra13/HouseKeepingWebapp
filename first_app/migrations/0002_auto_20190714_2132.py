# Generated by Django 2.1.4 on 2019-07-14 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='taskToBePerformedBy',
        ),
        migrations.RemoveField(
            model_name='task',
            name='timeOfAllocation',
        ),
    ]
