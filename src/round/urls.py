from django.urls import path
from round.views import RoundList, RoundCreate, RoundUpdate, RoundDetail
from match.views import MatchView

app_name = "rounds"

urlpatterns = [
	path('<pk>', RoundDetail.as_view(), name="detail"),
	path('create/', RoundCreate.as_view(), name="create"),
	path('update/<pk>', RoundUpdate.as_view(), name="update"),
	path('<pk>/match/', MatchView.as_view(), name="matches"),
]
