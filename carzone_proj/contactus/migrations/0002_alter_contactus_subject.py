# Generated by Django 4.0.3 on 2022-04-21 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]