# Generated by Django 4.1.9 on 2023-09-28 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HamkavDashboard', '0021_remove_chartmodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='chartmodel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chart_category', to='HamkavDashboard.category'),
        ),
    ]
