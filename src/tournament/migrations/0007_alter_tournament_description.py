# Generated by Django 4.0.5 on 2022-06-21 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0006_remove_tournament_players_tournament_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='description',
            field=models.CharField(max_length=128),
        ),
    ]
