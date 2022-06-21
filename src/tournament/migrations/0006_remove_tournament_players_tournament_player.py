# Generated by Django 4.0.5 on 2022-06-21 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_remove_player_tournaments'),
        ('tournament', '0005_alter_tournament_players'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='players',
        ),
        migrations.AddField(
            model_name='tournament',
            name='player',
            field=models.ManyToManyField(blank=True, related_name='player', to='player.player'),
        ),
    ]
