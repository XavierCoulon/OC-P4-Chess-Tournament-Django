from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from tournament.models import Tournament
from tournament.forms import TournamentSearch


def menu(request):
	return render(request, "tournament/tournament_menu.html")


class TournamentView(ListView):
	model = Tournament
	context_object_name = "tournaments"


class TournamentDetail(DetailView):
	model = Tournament
	context_object_name = "tournament"
	fields = "__all__"


class TournamentCreate(CreateView):
	model = Tournament
	template_name = "tournament/tournament_create_form.html"
	fields = "__all__"


class TournamentUpdate(UpdateView):
	model = Tournament
	template_name = "tournament/tournament_update_form.html"
	fields = "__all__"


def search(request):
	if request.method == 'POST':
		form = TournamentSearch(request.POST)
		if form.is_valid():
			return redirect("tournaments:detail", pk=form.cleaned_data["search"].pk)
	else:
		form = TournamentSearch()
	return render(request, "tournament/tournament_search.html", {"form": form})
