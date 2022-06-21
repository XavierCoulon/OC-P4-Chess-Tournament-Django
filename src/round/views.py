from django.views.generic import ListView, CreateView, UpdateView
from round.models import Round


class RoundView(ListView):
	model = Round
	context_object_name = "rounds"


class RoundCreate(CreateView):
	model = Round
	fields = "__all__"


class RoundUpdate(UpdateView):
	model = Round
	fields = "__all__"
