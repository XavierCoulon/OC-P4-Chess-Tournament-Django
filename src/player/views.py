from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from player.models import Player
from player.forms import PlayerSearch


def menu(request):
	return render(request, "player/player_menu.html")


def ranking(request):
	return render(request, "player/player_menu.html")


class PlayerView(ListView):
	model = Player
	context_object_name = "players"


class PlayerCreate(CreateView):
	model = Player
	template_name = "player/player_create_form.html"
	fields = "__all__"


class PlayerUpdate(UpdateView):
	model = Player
	template_name = "player/player_update_form.html"
	fields = "__all__"


def search(request):
	if request.method == 'POST':
		form = PlayerSearch(request.POST)
		if form.is_valid():
			return redirect("players:update", pk=form.cleaned_data["search"].pk)
	else:
		form = PlayerSearch()
	return render(request, "player/player_search.html", {"form": form})

