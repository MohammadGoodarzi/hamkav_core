# Generated by Django 4.1.9 on 2023-07-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HamkavBlog', '0027_alter_post_created_shamsi_alter_post_updated_shamsi'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
    ]
