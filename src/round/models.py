from django.db import models
from match.models import Match
from django.urls import reverse


class Round(models.Model):
	name = models.CharField(max_length=128, blank=False)
	start_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)
	tournament = models.ForeignKey(to='tournament.Tournament', on_delete=models.CASCADE, related_name="tournament")

	class Meta:
		unique_together = ["name", "tournament"]

	def save(self, *args, **kwargs):
		super(Round, self).save(*args, **kwargs)
		self.create_matches()

	def create_matches(self):
		players = self.tournament.player.all().order_by("ranking")

		if self.name == "Round 1":
			for first, second in zip(players, players[int(len(players) / 2):]):
				match = Match(
					round=self,
					player1=first,
					player1_score=0,
					player2=second,
					player2_score=0
				)
				match.save()
		else:
			players_list = []
			for player in players:
				players_list.append(player.score_ranking_tournament(self.tournament))
			sorted_players_list = sorted(players_list, key=lambda element: (-element[2], element[1]))
			for first, second in zip(sorted_players_list, sorted_players_list[int(len(sorted_players_list) / 2):]):
				match = Match(
					round=self,
					player1=first[0],
					player1_score=0,
					player2=second[0],
					player2_score=0
				)
				match.save()

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
