# Generated by Django 5.0.4 on 2024-05-21 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_role_rolename'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phoneNumber',
            field=models.CharField(default=123, max_length=10),
            preserve_default=False,
        ),
    ]
