# Generated by Django 3.2.6 on 2022-05-12 17:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20220512_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentprofile',
            old_name='desription',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='jobpostdata',
            name='application_deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 12, 17, 41, 19, 334213)),
        ),
    ]