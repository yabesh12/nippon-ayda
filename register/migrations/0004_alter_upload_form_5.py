# Generated by Django 3.2.4 on 2022-10-25 10:53

from django.db import migrations, models
import register.models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20221025_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='form_5',
            field=models.FileField(blank=True, null=True, upload_to=register.models.user_directory_path_for_rendering),
        ),
    ]