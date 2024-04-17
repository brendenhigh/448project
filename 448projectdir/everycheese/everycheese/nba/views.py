from django.views.generic import ListView, DetailView

from .models import Team, Match

class TeamListView(ListView):
	model = Team

class MatchListView(ListView):
    model = Match

class MatchDetailView(DetailView):
    model = Match

class TeamDetailView(DetailView):
	model = Team