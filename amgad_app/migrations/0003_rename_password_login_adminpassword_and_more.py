# Generated by Django 4.0.4 on 2022-05-18 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amgad_app', '0002_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='password',
            new_name='adminpassword',
        ),
        migrations.RenameField(
            model_name='login',
            old_name='username',
            new_name='adminusername',
        ),
    ]