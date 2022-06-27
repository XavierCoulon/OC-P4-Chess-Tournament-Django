from django.views.generic import ListView, CreateView, UpdateView
from match.models import Match


class MatchView(ListView):
	model = Match
	context_object_name = "matches"

	def get_queryset(self, *args, **kwargs):
		return Match.objects.filter(round_id=self.kwargs.get("pk"))


class MatchCreate(CreateView):
	model = Match
	fields = "__all__"


class MatchResult(UpdateView):
	model = Match
	template_name = "match/match_result_form.html"
	fields = ["player1_score", "player2_score"]
