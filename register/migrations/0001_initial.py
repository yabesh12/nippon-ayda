# Generated by Django 3.2.4 on 2021-07-29 18:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('College', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=10, null=True)),
                ('Name', models.CharField(max_length=225)),
                ('E_Mail', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message='Chek you Email')], verbose_name='E Mail')),
                ('Phone', models.CharField(max_length=10, unique=True)),
                ('Study_Year', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=100, verbose_name='Study Year')),
                ('Year_of_Graduation', models.CharField(choices=[('1', '2021'), ('2', '2022'), ('3', '2023'), ('4', '2024'), ('5', '2025')], max_length=100, verbose_name='Year of Graduation')),
                ('Category', models.CharField(choices=[('Architecture', 'Architecture'), ('Interior Design', 'Interior Design')], max_length=225)),
                ('Date_time', models.DateTimeField(auto_now=True)),
                ('College', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='register.college')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_1', models.FileField(upload_to='projects/')),
                ('form_2', models.FileField(blank=True, null=True, upload_to='projects/')),
                ('form_3', models.FileField(blank=True, null=True, upload_to='projects/')),
                ('form_4', models.FileField(blank=True, null=True, upload_to='projects/')),
                ('form_5', models.FileField(blank=True, null=True, upload_to='projects/')),
                ('uuid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='register.registerform')),
            ],
        ),
        migrations.AddField(
            model_name='registerform',
            name='states',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='register.state', verbose_name='State'),
        ),
    ]