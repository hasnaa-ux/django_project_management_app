# Generated by Django 4.0.4 on 2022-05-25 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amgad_app', '0017_alter_appointment_yourdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='YourDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 25, 13, 8, 39, 665605), null=True, verbose_name='Date'),
        ),
    ]