# Generated by Django 4.0.4 on 2022-05-25 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amgad_app', '0019_alter_appointment_yourdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='YourDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 25, 14, 35, 2, 149861), null=True, verbose_name='Date'),
        ),
    ]