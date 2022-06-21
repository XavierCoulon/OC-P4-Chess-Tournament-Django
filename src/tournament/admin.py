from django.contrib import admin
from tournament.models import Tournament, GameType


admin.site.register(Tournament)
admin.site.register(GameType)
