# Generated by Django 2.2.5 on 2021-04-19 04:20

import core.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210307_1410'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', core.managers.CustomUserManager()),
            ],
        ),
    ]
