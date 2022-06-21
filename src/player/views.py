from django.views.generic import ListView, CreateView, UpdateView
from player.models import Player


class PlayerView(ListView):
	model = Player
	context_object_name = "players"


class PlayerCreate(CreateView):
	model = Player
	fields = "__all__"


class PlayerUpdate(UpdateView):
	model = Player
	fields = "__all__"
