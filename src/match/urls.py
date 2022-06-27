from django.urls import path
from match.views import MatchView, MatchCreate, MatchResult

app_name = "matches"

urlpatterns = [
	path('', MatchView.as_view(), name="list"),
	path('create/', MatchCreate.as_view(), name="create"),
	path('result/<int:pk>', MatchResult.as_view(), name="result"),
]
