# Generated by Django 3.1.1 on 2024-04-26 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nba', '0003_team_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='teams',
        ),
    ]
