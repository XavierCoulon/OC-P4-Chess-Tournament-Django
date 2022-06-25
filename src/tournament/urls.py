from django.urls import path
from tournament.views import TournamentView, TournamentCreate, TournamentUpdate, TournamentDetail, search, menu, create_round
from round.views import RoundList

app_name = "tournaments"

urlpatterns = [
	path('', menu, name="menu"),
	path('list/', TournamentView.as_view(), name="list"),
	path('<pk>', TournamentDetail.as_view(), name="detail"),
	path('create/', TournamentCreate.as_view(), name="create"),
	path('<pk>/update', TournamentUpdate.as_view(), name="update"),

	path('search/', search, name="search"),
	path('<pk>/round/', RoundList.as_view(), name="rounds"),
	path('<pk>/create_round/', create_round, name="create_round"),

	# path('<pk>/rounds/<round_id>/', matches_list, name="matches"),
	# path('<pk>/matches', matches_list, name="matches")
	# path('<pk>/round/', include("round.urls")),
]
