# Generated by Django 3.2.6 on 2022-03-16 02:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20220312_0113'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.AlterField(
            model_name='jobpostdata',
            name='application_deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 16, 2, 22, 27, 801505)),
        ),
    ]
