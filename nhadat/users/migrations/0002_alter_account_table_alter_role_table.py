# Generated by Django 5.0.4 on 2024-05-19 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='account',
            table='Accounts',
        ),
        migrations.AlterModelTable(
            name='role',
            table='Roles',
        ),
    ]
