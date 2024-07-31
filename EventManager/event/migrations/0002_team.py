# Generated by Django 5.0.6 on 2024-07-06 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Picture', models.ImageField(upload_to='team/')),
                ('Description', models.CharField(max_length=400)),
            ],
        ),
    ]