# Generated by Django 3.2.4 on 2021-08-16 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='college',
            options={'ordering': ('College',)},
        ),
    ]
