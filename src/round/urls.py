from django.urls import path
from round.views import RoundView, RoundCreate, RoundUpdate

app_name = "rounds"

urlpatterns = [
	path('', RoundView.as_view(), name="home"),
	path('create/', RoundCreate.as_view(), name="create"),
	path('update/<int:pk>', RoundUpdate.as_view(), name="update"),
]
