# Generated by Django 4.0.3 on 2022-06-30 00:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amgad_app', '0032_alter_appointment_yourdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='YourDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 30, 2, 22, 20, 100904), null=True, verbose_name='Date'),
        ),
    ]
