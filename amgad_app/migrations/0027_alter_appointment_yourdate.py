# Generated by Django 4.0.4 on 2022-06-03 17:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amgad_app', '0026_login_signup_alter_appointment_yourdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='YourDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 3, 19, 18, 34, 325889), null=True, verbose_name='Date'),
        ),
    ]
