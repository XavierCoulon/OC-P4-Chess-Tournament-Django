from django.db import models
from django.urls import reverse


class Match(models.Model):
	round = models.ForeignKey(to='round.Round', on_delete=models.CASCADE, related_name="round")
	player1 = models.ForeignKey(to='player.Player', on_delete=models.CASCADE, related_name="player1")
	player2 = models.ForeignKey(to='player.Player', on_delete=models.CASCADE, related_name="player2")
	player1_score = models.FloatField()
	player2_score = models.FloatField()

	def get_absolute_url(self):
		return reverse("rounds:detail", kwargs={"pk": self.round_id})
