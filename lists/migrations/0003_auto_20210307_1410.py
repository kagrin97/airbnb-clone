# Generated by Django 2.2.5 on 2021-03-07 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20210209_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to=settings.AUTH_USER_MODEL),
        ),
    ]
