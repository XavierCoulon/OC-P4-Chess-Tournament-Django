from django.urls import path
from player.views import PlayerView, PlayerCreate, PlayerUpdate, search, menu

app_name = "players"

urlpatterns = [
	path('', menu, name="menu"),
	path('search/', search, name="search"),
	path('list/', PlayerView.as_view(), name="list"),
	path('create/', PlayerCreate.as_view(), name="create"),
	path('update/<int:pk>', PlayerUpdate.as_view(), name="update"),
]
