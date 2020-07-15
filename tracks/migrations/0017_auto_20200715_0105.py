# Generated by Django 3.0.7 on 2020-07-15 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0016_playcount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playcount',
            name='id',
        ),
        migrations.AlterField(
            model_name='playcount',
            name='track',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tracks.Track'),
        ),
    ]
