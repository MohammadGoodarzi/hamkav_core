# Generated by Django 4.1.9 on 2023-07-05 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HamkavBlog', '0029_rename_is_active_post_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
