from django.db import models
# from tournament.models import Tournament
from django.urls import reverse


class Round(models.Model):
	name = models.CharField(max_length=128, blank=False)
	start_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)
	tournament = models.ForeignKey(to='tournament.Tournament', on_delete=models.CASCADE)

	class Meta:
		unique_together = ["name", "tournament"]

	def get_absolute_url(self):
		return reverse("rounds:home")

	def __str__(self):
		return self.name
