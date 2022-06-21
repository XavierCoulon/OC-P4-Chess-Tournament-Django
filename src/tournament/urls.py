from django.urls import path
from tournament.views import TournamentView, TournamentCreate, TournamentUpdate

app_name = "tournaments"

urlpatterns = [
	path('', TournamentView.as_view(), name="home"),
	path('create/', TournamentCreate.as_view(), name="create"),
	path('update/<int:pk>', TournamentUpdate.as_view(), name="update"),
]
