# Generated by Django 4.1.9 on 2023-06-30 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HamkavBlog', '0026_remove_post_body2_alter_post_created_shamsi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_shamsi',
            field=models.CharField(editable=False, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_shamsi',
            field=models.CharField(editable=False, max_length=50, null=True),
        ),
    ]
