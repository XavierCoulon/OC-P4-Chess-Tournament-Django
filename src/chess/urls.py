from django.contrib import admin
from django.urls import path, include


urlpatterns = [
	path('admin/', admin.site.urls),
	path('tournament/', include('tournament.urls')),
	path('player/', include('player.urls')),
	path('match/', include('match.urls')),
	path('round/', include('round.urls')),
]
