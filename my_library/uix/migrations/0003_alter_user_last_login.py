# Generated by Django 3.2 on 2021-04-13 22:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uix', '0002_auto_20210413_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 22, 41, 5, 703943, tzinfo=utc), verbose_name='User last login datetime'),
        ),
    ]
