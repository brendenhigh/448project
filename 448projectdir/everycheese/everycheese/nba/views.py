from django.views.generic import ListView, DetailView, UpdateView

from .models import Team, Match

from everycheese.users.models import User

from django.contrib.auth.mixins import LoginRequiredMixin

class TeamListView(ListView):
	model = Team

class MatchListView(ListView):
    model = Match

class MatchDetailView(DetailView):
    model = Match

class TeamDetailView(DetailView):
	model = Team

class TeamUpdateView(UpdateView):
	model = User

	fields = [
		'team',
	]
	
	action = "Update"

	def form_valid(self, form):
		form.instance.creator = self.request.user
		return super().form_valid(form)

