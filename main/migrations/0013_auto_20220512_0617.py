# Generated by Django 3.2.6 on 2022-05-12 06:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0012_alter_jobpostdata_application_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='user_profile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jobpostdata',
            name='application_deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 12, 6, 17, 9, 797584)),
        ),
    ]
