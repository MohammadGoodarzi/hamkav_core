# Generated by Django 4.1.9 on 2023-11-24 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HamkavDbManagement', '0014_alter_datasourcemodel_media_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasourcemodel',
            name='datasource_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HamkavDbManagement.datasourcetype'),
        ),
    ]
