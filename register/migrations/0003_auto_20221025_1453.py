# Generated by Django 3.2.4 on 2022-10-25 09:23

from django.db import migrations, models
import register.models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_college_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerform',
            name='Year_of_Graduation',
            field=models.CharField(choices=[('1', '2022'), ('2', '2023'), ('3', '2024'), ('4', '2025'), ('5', '2026')], max_length=100, verbose_name='Year of Graduation'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='form_1',
            field=models.FileField(null=True, upload_to=register.models.user_directory_path_for_presentation),
        ),
        migrations.AlterField(
            model_name='upload',
            name='form_2',
            field=models.FileField(null=True, upload_to=register.models.user_directory_path_for_statement),
        ),
        migrations.AlterField(
            model_name='upload',
            name='form_3',
            field=models.FileField(null=True, upload_to=register.models.user_directory_path_for_concept),
        ),
        migrations.AlterField(
            model_name='upload',
            name='form_4',
            field=models.FileField(blank=True, null=True, upload_to=register.models.user_directory_path_for_photo),
        ),
        migrations.AlterField(
            model_name='upload',
            name='form_5',
            field=models.FileField(blank=True, null=True, upload_to=register.models.user_directory_path_for_photo),
        ),
    ]
