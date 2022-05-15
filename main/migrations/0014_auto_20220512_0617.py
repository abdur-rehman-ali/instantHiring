# Generated by Django 3.2.6 on 2022-05-12 06:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0013_auto_20220512_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpostdata',
            name='application_deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 12, 6, 17, 36, 25597)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
