# Generated by Django 2.1.4 on 2019-07-14 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('timeOfAllocation', models.DateTimeField(auto_now_add=True)),
                ('taskToBePerformedBy', models.DateTimeField(auto_now_add=True)),
                ('frequency', models.CharField(choices=[('hourly', 'hourly'), ('daily', 'daily'), ('weekly', 'weekly'), ('monthly', 'monthly'), ('yearly', 'yearly')], default='hourly', max_length=50)),
                ('assetid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workerid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='workerid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='first_app.Worker'),
        ),
    ]