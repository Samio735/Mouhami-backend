# Generated by Django 5.0.1 on 2024-01-05 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mouhami_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='review',
        ),
        migrations.AddField(
            model_name='review',
            name='booking',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mouhami_api.booking'),
            preserve_default=False,
        ),
    ]
