from django.db import models
from django.urls import reverse

from round.models import Round
from player.models import Player


class Match(models.Model):
	round = models.ForeignKey(to=Round, on_delete=models.CASCADE, related_name="round")
	player1 = models.ForeignKey(to=Player, on_delete=models.CASCADE, related_name="player1")
	player2 = models.ForeignKey(to=Player, on_delete=models.CASCADE, related_name="player2")
	player1_score = models.FloatField()
	player2_score = models.FloatField()

	def get_absolute_url(self):
		return reverse("matches:home")
