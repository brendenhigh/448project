from django.views.generic import ListView, DetailView, CreateView

from .models import Team, Match, UserTeam

from django.contrib.auth.mixins import LoginRequiredMixin

class TeamListView(ListView):
	model = Team

class MatchListView(ListView):
    model = Match

class MatchDetailView(DetailView):
    model = Match

class TeamDetailView(DetailView):
	model = Team

class TeamCreateView(LoginRequiredMixin, CreateView):
	model = Team

	fields = [
		'team_name',
		'created_date',
	]

	
