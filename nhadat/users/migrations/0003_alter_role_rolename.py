# Generated by Django 5.0.4 on 2024-05-21 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_account_table_alter_role_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='roleName',
            field=models.CharField(max_length=20),
        ),
    ]
