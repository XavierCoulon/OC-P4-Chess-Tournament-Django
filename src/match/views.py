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


class MatchUpdate(UpdateView):
	model = Match
	fields = "__all__"
