from django.db import models
from tournament.models import Tournament
from django.urls import reverse


class Round(models.Model):
	name = models.CharField(unique=True, max_length=128, blank=False)
	start_date = models.DateField(blank=False)
	end_date = models.DateField(blank=False)
	tournament = models.ForeignKey(to=Tournament, on_delete=models.CASCADE)

	class Meta:
		unique_together = ["name", "tournament"]

	def get_absolute_url(self):
		return reverse("rounds:home")

	def __str__(self):
		return self.name
