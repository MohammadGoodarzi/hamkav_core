# Generated by Django 4.1.9 on 2023-08-30 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HamkavDbManagement', '0006_databasetype_created_shamsi_and_more'),
        ('HamkavDashboard', '0002_chartmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='chartmodel',
            name='chart_type_access',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='chartmodel',
            name='chart_type_id',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='chartmodel',
            name='chart_type_title',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='chartmodel',
            name='datasource',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HamkavDbManagement.datasourcemodel'),
        ),
        migrations.AddField(
            model_name='chartmodel',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='layoutmodel',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='chartmodel',
            name='chart_base_config',
            field=models.JSONField(blank=True, max_length=100, null=True),
        ),
    ]
