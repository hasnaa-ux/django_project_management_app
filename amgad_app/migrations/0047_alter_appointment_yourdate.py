# Generated by Django 4.0.3 on 2022-07-11 18:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amgad_app', '0046_alter_appointment_yourdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='YourDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 11, 20, 59, 46, 896440), null=True, verbose_name='Date'),
        ),
    ]