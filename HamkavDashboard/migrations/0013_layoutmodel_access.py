# Generated by Django 4.1.9 on 2023-09-05 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HamkavDashboard', '0012_charttypemodel_meta_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='layoutmodel',
            name='access',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
