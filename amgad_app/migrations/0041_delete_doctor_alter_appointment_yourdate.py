# Generated by Django 4.0.3 on 2022-07-02 23:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amgad_app', '0040_alter_appointment_yourdate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='YourDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 3, 1, 22, 48, 779227), null=True, verbose_name='Date'),
        ),
    ]