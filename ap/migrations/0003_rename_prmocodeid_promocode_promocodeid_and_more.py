# Generated by Django 5.0.4 on 2024-04-17 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0002_promocode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promocode',
            old_name='prmocodeid',
            new_name='promocodeid',
        ),
        migrations.AlterField(
            model_name='promocode',
            name='code',
            field=models.CharField(max_length=100),
        ),
    ]
