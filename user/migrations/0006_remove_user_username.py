# Generated by Django 4.1.10 on 2023-09-01 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
