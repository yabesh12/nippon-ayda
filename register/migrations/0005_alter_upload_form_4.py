# Generated by Django 3.2.4 on 2022-10-25 11:51

from django.db import migrations, models
import register.models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_alter_upload_form_5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='form_4',
            field=models.ImageField(blank=True, null=True, upload_to=register.models.user_directory_path_for_photo),
        ),
    ]
