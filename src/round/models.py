from django.db import models
from match.models import Match
from django.urls import reverse


class Round(models.Model):
	name = models.CharField(max_length=128, blank=False)
	start_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)
	tournament = models.ForeignKey(to='tournament.Tournament', on_delete=models.CASCADE)

	class Meta:
		unique_together = ["name", "tournament"]

	def save(self, *args, **kwargs):
		super(Round, self).save(*args, **kwargs)
		print("Créer les matches ici /!/")

	def get_absolute_url(self):
		return reverse("rounds:home")

	def __str__(self):
		return self.name

	def is_resulted(self):
		matches = Match.objects.filter(round_id=self.pk)
		sum_score = [(match.player1_score + match.player2_score) for match in matches]
		if sum(sum_score) == len(matches):
			return True
		return False
