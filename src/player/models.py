from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Sum
from django.urls import reverse

from round.models import Round
from match.models import Match


class Gender(models.Model):
	label = models.CharField(unique=True, max_length=128)


class Player(models.Model):
	first_name = models.CharField(unique=True, max_length=128, blank=False)
	last_name = models.CharField(unique=True, max_length=128, blank=False)
	ranking = models.PositiveIntegerField(unique=True, validators=[MinValueValidator(1)])
	birth_date = models.DateField(blank=False)
	gender = models.ForeignKey(to=Gender, on_delete=models.PROTECT)
	description = models.CharField(unique=True, max_length=128, blank=False)

	def score_ranking_tournament(self, tournament):
		score_if_player1 = Match.objects.filter(player1=self, round__tournament=tournament).aggregate(Sum("player1_score"))
		score_if_player2 = Match.objects.filter(player2=self, round__tournament=tournament).aggregate(Sum("player2_score"))

		return [self, sum(filter(None, [score_if_player1["player1_score__sum"], score_if_player2["player2_score__sum"]])), self.ranking]

	def get_absolute_url(self):
		return reverse("players:menu")

	def __str__(self):
		return self.first_name
