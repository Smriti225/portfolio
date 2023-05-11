# Generated by Django 3.2.12 on 2023-05-10 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='verification_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('code', models.IntegerField(max_length=4)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2023, 5, 10, 7, 27, 33, 739402))),
                ('expiry_on', models.DateTimeField(default=datetime.datetime(2023, 5, 10, 7, 30, 33, 739460))),
            ],
        ),
    ]