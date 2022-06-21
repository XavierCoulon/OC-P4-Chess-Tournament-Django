from django.urls import path
from player.views import PlayerView, PlayerCreate, PlayerUpdate

app_name = "players"

urlpatterns = [
	path('', PlayerView.as_view(), name="home"),
	path('create/', PlayerCreate.as_view(), name="create"),
	path('update/<int:pk>', PlayerUpdate.as_view(), name="update"),
]
