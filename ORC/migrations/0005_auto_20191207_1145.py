# Generated by Django 2.1.5 on 2019-12-07 17:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ORC', '0004_auto_20191207_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_purchasedate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
