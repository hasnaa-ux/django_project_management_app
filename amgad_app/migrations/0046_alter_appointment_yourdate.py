# Generated by Django 4.0.3 on 2022-07-11 18:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amgad_app', '0045_rename_yourdepartment_appointment_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='YourDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 11, 20, 53, 55, 867423), null=True, verbose_name='Date'),
        ),
    ]
