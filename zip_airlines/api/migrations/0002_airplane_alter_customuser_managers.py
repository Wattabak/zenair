# Generated by Django 4.1 on 2022-08-26 13:12

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('fuel_capacity', models.FloatField(blank=True, null=True)),
                ('base_fuel_consumption', models.FloatField(blank=True, null=True)),
                ('passenger_capacity', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
