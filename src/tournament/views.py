from django.views.generic import ListView, CreateView, UpdateView
from tournament.models import Tournament


class TournamentView(ListView):
	model = Tournament
	context_object_name = "tournaments"


class TournamentCreate(CreateView):
	model = Tournament
	fields = "__all__"


class TournamentUpdate(UpdateView):
	model = Tournament
	fields = "__all__"
