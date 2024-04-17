from django.urls import path
from . import views

app_name = "nba"
urlpatterns = [
	path (
		route='',
		view=views.TeamListView.as_view(),
		name='team_list'
	),
]