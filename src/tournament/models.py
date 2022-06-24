from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse

from player.models import Player
from round.models import Round


class GameType(models.Model):
	label = models.CharField(unique=True, max_length=128, blank=False)


class Tournament(models.Model):
	name = models.CharField(unique=True, max_length=128, blank=False)
	location = models.CharField(max_length=128, blank=False)
	game_type = models.ForeignKey(to=GameType, on_delete=models.PROTECT)
	dates = ArrayField(models.DateField(blank=False))
	description = models.CharField(max_length=128, blank=False)
	player = models.ManyToManyField(to=Player, related_name="player", blank=True)

	def get_absolute_url(self):
		return reverse("tournaments:menu")

	def __str__(self):
		return self.name

	def create_round(self):
		round = Round(tournament_id=self.pk)
		print(round)


