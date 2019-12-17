# Generated by Django 2.1.5 on 2019-12-17 04:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ORC', '0017_auto_20191216_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomallotment',
            name='allotment_enddate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 17, 4, 1, 6, 621380, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roomallotment',
            name='allotment_startdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 17, 4, 1, 6, 621356, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='workorder_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]