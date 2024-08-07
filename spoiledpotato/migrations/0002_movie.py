# Generated by Django 5.0.8 on 2024-08-07 14:15

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spoiledpotato', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('length', models.DurationField()),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('preview_url', models.TextField()),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='spoiledpotato.actor')),
            ],
        ),
    ]
