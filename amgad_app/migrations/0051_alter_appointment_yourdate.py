# Generated by Django 4.0.3 on 2022-07-12 00:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amgad_app', '0050_alter_appointment_yourdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='YourDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 12, 2, 19, 18, 835942), null=True, verbose_name='Date'),
        ),
    ]