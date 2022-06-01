# Generated by Django 4.0.3 on 2022-04-17 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_teams_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('number', models.IntegerField()),
                ('subject', models.TextField(max_length=500)),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]