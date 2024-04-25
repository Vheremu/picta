# Generated by Django 5.0.4 on 2024-04-17 07:14

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
            name='Add',
            fields=[
                ('addid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(upload_to='static/adds')),
                ('cost', models.IntegerField()),
                ('payout', models.IntegerField()),
                ('company', models.CharField(blank=True, max_length=100)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]