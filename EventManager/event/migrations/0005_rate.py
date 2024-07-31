# Generated by Django 5.0.6 on 2024-07-10 06:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=700)),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.work')),
            ],
        ),
    ]
