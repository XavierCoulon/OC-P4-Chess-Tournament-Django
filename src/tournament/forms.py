from django.forms import ModelForm, ModelChoiceField
from tournament.models import Tournament


class TournamentSearch(ModelForm):
	search = ModelChoiceField(queryset=Tournament.objects.all())

	class Meta:
		model = Tournament
		fields = ("search",)






