# Generated by Django 4.1.9 on 2023-06-20 11:37

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('HamkavBlog', '0004_blogcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='HamkavBlog.blogcategory'),
        ),
    ]
