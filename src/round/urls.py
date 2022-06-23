from django.urls import path, include
from round.views import RoundList, RoundCreate, RoundUpdate, RoundDetail

app_name = "rounds"

urlpatterns = [
	path('', RoundList.as_view(), name="list"),
	path('<pk>', RoundDetail.as_view(), name="detail"),
	path('<pk>/match/', include("match.urls", namespace="matches")),
	path('create/', RoundCreate.as_view(), name="create"),
	path('update/<pk>', RoundUpdate.as_view(), name="update"),
]
