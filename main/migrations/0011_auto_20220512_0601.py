# Generated by Django 3.2.6 on 2022-05-12 06:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20220317_0213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='facebook_url',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='github_url',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='instagram_url',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='linkedin_url',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='website_url',
        ),
        migrations.AlterField(
            model_name='jobpostdata',
            name='application_deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 12, 6, 1, 19, 222955)),
        ),
    ]
