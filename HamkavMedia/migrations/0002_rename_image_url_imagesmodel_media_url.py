# Generated by Django 4.1.9 on 2023-11-20 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HamkavMedia', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagesmodel',
            old_name='image_url',
            new_name='media_url',
        ),
    ]
