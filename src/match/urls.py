from django.urls import path
from match.views import MatchView, MatchCreate, MatchUpdate

app_name = "matches"

urlpatterns = [
	path('', MatchView.as_view(), name="home"),
	path('create/', MatchCreate.as_view(), name="create"),
	path('update/<int:pk>', MatchUpdate.as_view(), name="update"),
]
