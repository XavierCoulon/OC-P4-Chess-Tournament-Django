from django.urls import path, include
from tournament.views import TournamentView, TournamentCreate, TournamentUpdate, TournamentDetail, search, menu
from round.views import RoundList

app_name = "tournaments"

urlpatterns = [
	path('', menu, name="menu"),
	path('list/', TournamentView.as_view(), name="list"),
	path('search/', search, name="search"),
	path('<pk>', TournamentDetail.as_view(), name="detail"),
	path('<pk>/round/', include("round.urls", namespace="rounds")),
	path('create/', TournamentCreate.as_view(), name="create"),
	path('update/<pk>', TournamentUpdate.as_view(), name="update"),
	path('<pk>/rounds', RoundList.as_view(), name="rounds"),
]
