# Generated by Django 3.2.3 on 2021-05-24 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
