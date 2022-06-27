from django.views.generic import ListView, CreateView, UpdateView, DetailView
from round.models import Round


class RoundList(ListView):
	model = Round
	context_object_name = "rounds"

	def get_queryset(self, *args, **kwargs):
		return Round.objects.filter(tournament_id=self.kwargs.get("pk"))


class RoundDetail(DetailView):
	model = Round
	context_object_name = "round"
	fields = "__all__"


class RoundCreate(CreateView):
	model = Round
	fields = "__all__"


class RoundUpdate(UpdateView):
	model = Round
	fields = "__all__"
