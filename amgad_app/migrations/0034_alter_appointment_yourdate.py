# Generated by Django 4.0.3 on 2022-06-30 00:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amgad_app', '0033_alter_appointment_yourdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='YourDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 30, 2, 27, 0, 785270), null=True, verbose_name='Date'),
        ),
    ]
