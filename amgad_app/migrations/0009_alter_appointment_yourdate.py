# Generated by Django 4.0.4 on 2022-05-20 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amgad_app', '0008_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='YourDate',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
