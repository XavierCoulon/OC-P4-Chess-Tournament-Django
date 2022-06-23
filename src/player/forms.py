from django.forms import ModelForm, ModelChoiceField
from player.models import Player


class PlayerSearch(ModelForm):
	search = ModelChoiceField(queryset=Player.objects.all())

	class Meta:
		model = Player
		fields = ("search",)






