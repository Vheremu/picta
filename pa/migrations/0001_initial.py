# Generated by Django 4.2.7 on 2024-02-23 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "taskid",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
                ("name", models.CharField(blank=True, max_length=100)),
                ("description", models.CharField(blank=True, max_length=100)),
                ("frequency", models.CharField(blank=True, max_length=100)),
                ("time", models.IntegerField(blank=True)),
                ("cost", models.IntegerField(blank=True)),
                ("nature", models.CharField(max_length=50)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]