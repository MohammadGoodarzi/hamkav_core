# Generated by Django 4.1.9 on 2024-01-12 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HamkavDbManagement', '0015_alter_datasourcemodel_datasource_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasourcemodel',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True, unique=True),
        ),
    ]