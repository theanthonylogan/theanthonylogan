# Generated by Django 4.2.7 on 2023-11-18 20:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('db', '0002_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('notes', models.TextField()),
                ('completed', models.BooleanField()),
                ('due_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 11, 18, 20, 54, 16, 354144, tzinfo=datetime.timezone.utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2023, 11, 18, 20, 54, 16, 354171, tzinfo=datetime.timezone.utc))),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]