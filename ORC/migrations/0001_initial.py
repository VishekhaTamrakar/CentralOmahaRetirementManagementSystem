# Generated by Django 2.1.5 on 2019-11-01 00:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipId', models.IntegerField()),
                ('equipName', models.CharField(max_length=100)),
                ('equipDescription', models.CharField(blank=True, max_length=200)),
                ('equipMaintCost', models.IntegerField(blank=True, null=True)),
                ('equipUnitCost', models.IntegerField(blank=True, null=True)),
                ('equipUnitStock', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mwId', models.IntegerField()),
                ('mwDescription', models.CharField(max_length=100)),
                ('mwWorkCost', models.IntegerField(blank=True, null=True)),
                ('mwStartDateTime', models.DateTimeField()),
                ('mwEndDateTime', models.DateTimeField(blank=True, null=True)),
                ('is_open', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenanceworks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyId', models.IntegerField()),
                ('propertyName', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=100)),
                ('roomNumber', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=30)),
                ('zipCode', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Workorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('woId', models.IntegerField()),
                ('woDescription', models.CharField(max_length=100)),
                ('woPriority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('critical', 'Critical')], default='low', max_length=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('woStartDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('woEndDate', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('is_open', models.BooleanField(default=True)),
                ('roomNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workorders', to='ORC.PropertyLocation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workorders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='maintenancework',
            name='woId',
            field=models.ForeignKey(default=999, on_delete=django.db.models.deletion.CASCADE, related_name='maintenanceworks', to='ORC.Workorder'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='mwId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipments', to='ORC.MaintenanceWork'),
        ),
    ]
