# Generated by Django 2.1.5 on 2019-12-17 03:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ORC', '0014_auto_20191216_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomallotment',
            name='allotment_enddate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 17, 3, 9, 34, 289151, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roomallotment',
            name='allotment_startdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 17, 3, 9, 34, 289125, tzinfo=utc)),
        ),
    ]