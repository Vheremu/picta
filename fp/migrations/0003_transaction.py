# Generated by Django 5.0.4 on 2024-04-08 19:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fp', '0002_alter_pop_pop'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transactionid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('transactiontype', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(null=True, verbose_name='date')),
                ('reference', models.CharField(blank=True, max_length=50)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('staffid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffid', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]