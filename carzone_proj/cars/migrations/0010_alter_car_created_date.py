# Generated by Django 4.0.3 on 2022-05-03 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_alter_car_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 3, 17, 11, 6, 954397)),
        ),
    ]
