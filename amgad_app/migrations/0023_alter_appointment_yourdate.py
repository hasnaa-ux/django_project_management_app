# Generated by Django 4.0.4 on 2022-06-01 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amgad_app', '0022_alter_appointment_yourdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='YourDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 1, 15, 52, 9, 720134), null=True, verbose_name='Date'),
        ),
    ]
