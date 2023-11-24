# Generated by Django 4.1.9 on 2023-11-21 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HamkavMedia', '0003_mediamodel_rename_imagetypemodel_mediatypemodel_and_more'),
        ('HamkavDbManagement', '0008_alter_datasourcemodel_query_string'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasourcemodel',
            name='media_source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HamkavMedia.mediamodel'),
        ),
    ]
