# Generated by Django 3.2.12 on 2023-05-10 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20230510_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification_code',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 7, 36, 38, 119198)),
        ),
        migrations.AlterField(
            model_name='verification_code',
            name='expiry_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 7, 39, 38, 119255)),
        ),
    ]