# Generated by Django 3.2.6 on 2022-03-12 00:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220312_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpostdata',
            name='application_deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 12, 0, 41, 27, 502969)),
        ),
    ]
