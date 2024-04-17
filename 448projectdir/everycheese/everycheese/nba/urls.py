from django.urls import path
from . import views

app_name = "nba"
urlpatterns = [
	path (
		route='',
		view=views.TeamListView.as_view(),
		name='team_list'
	),
    path (
        route='<slug:slug>',
        view=views.TeamDetailView.as_view(),
        name='team_detail'
	)
]