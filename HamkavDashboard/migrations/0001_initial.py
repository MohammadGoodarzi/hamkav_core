# Generated by Django 4.1.9 on 2023-08-24 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LayoutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('title', models.CharField(max_length=300)),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('layout_config', models.JSONField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_shamsi', models.CharField(editable=False, max_length=50, null=True)),
                ('updated_shamsi', models.CharField(editable=False, max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
