# Generated by Django 4.1.9 on 2023-06-29 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HamkavBlog', '0023_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_shamsi',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_shamsi',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
