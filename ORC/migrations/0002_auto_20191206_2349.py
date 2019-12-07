# Generated by Django 2.1.5 on 2019-12-07 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ORC', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancework',
            name='residentid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residentid', to='ORC.Resident'),
        ),
        migrations.AlterField(
            model_name='maintenancework',
            name='residentname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residentname', to='ORC.Resident'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='resident_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resid', to='ORC.Resident'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='resident_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resname', to='ORC.Resident'),
        ),
    ]
