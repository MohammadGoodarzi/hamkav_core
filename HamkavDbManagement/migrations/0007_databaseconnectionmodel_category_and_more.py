# Generated by Django 4.1.9 on 2023-10-03 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HamkavConfigurator', '0003_alter_category_options_alter_category_type2_options'),
        ('HamkavDbManagement', '0006_databasetype_created_shamsi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='databaseconnectionmodel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='database_category', to='HamkavConfigurator.category_type2'),
        ),
        migrations.AddField(
            model_name='datasourcemodel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='datasource_category', to='HamkavConfigurator.category_type2'),
        ),
    ]