# Generated by Django 4.0.3 on 2022-06-01 13:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_alter_car_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('title_1', models.CharField(max_length=50)),
                ('content_1', models.CharField(max_length=100)),
                ('banner_image_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('title_2', models.CharField(max_length=100)),
                ('content_2', models.CharField(max_length=100)),
                ('banner_image_3', models.ImageField(blank=True, upload_to='ohotos/%Y/%m/%d')),
                ('title_3', models.CharField(max_length=50)),
                ('content_3', models.CharField(max_length=100)),
                ('is_feature', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 1, 19, 10, 19, 224858))),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 1, 19, 10, 19, 224858)),
        ),
    ]