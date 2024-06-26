# Generated by Django 5.0.4 on 2024-04-08 08:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pop',
            fields=[
                ('popid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('pop', models.ImageField(blank=True, upload_to='static/pops')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
