from django.urls import path
from . import views

app_name = "nba"
urlpatterns = [
    path(
        route='matches/', 
        view=views.MatchListView.as_view(), 
        name='match_list'
    ),
	path (
		route='',
		view=views.TeamListView.as_view(),
		name='team_list'
	),
     path(
        route='matches/<slug:slug>/', 
        view=views.MatchDetailView.as_view(), 
        name='match_detail'
    ),
    path (
        route='<slug:slug>',
        view=views.TeamDetailView.as_view(),
        name='team_detail'
	)
]