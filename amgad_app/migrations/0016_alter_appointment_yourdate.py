# Generated by Django 4.0.4 on 2022-05-22 06:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amgad_app', '0015_alter_appointment_yourdate_alter_doctor_bio_doctor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='YourDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 22, 8, 33, 11, 407332), null=True, verbose_name='Date'),
        ),
    ]