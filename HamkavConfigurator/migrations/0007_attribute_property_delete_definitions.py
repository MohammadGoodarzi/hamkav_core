# Generated by Django 4.1.9 on 2024-01-12 04:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HamkavConfigurator', '0006_alter_definitions_def_id_alter_definitions_def_zone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='attribute',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_shamsi', models.CharField(editable=False, max_length=50, null=True)),
                ('updated_shamsi', models.CharField(editable=False, max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=300)),
                ('item_code', models.PositiveIntegerField(null=True)),
                ('item_name', models.CharField(blank=True, max_length=300)),
                ('user_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='property',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_shamsi', models.CharField(editable=False, max_length=50, null=True)),
                ('updated_shamsi', models.CharField(editable=False, max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=300)),
                ('item_code', models.PositiveIntegerField(null=True)),
                ('item_name', models.CharField(blank=True, max_length=300)),
                ('user_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Definitions',
        ),
    ]