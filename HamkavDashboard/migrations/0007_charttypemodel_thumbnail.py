# Generated by Django 4.1.9 on 2023-08-31 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HamkavDashboard', '0006_rename_chart_type_title_chartmodel_access_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='charttypemodel',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='attach/%Y/%m/%d'),
        ),
    ]
