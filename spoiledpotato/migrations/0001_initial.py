# Generated by Django 5.0.8 on 2024-08-07 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('photo_url', models.TextField()),
            ],
        ),
    ]
