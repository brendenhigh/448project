from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from django.urls import reverse
from django.conf import settings


class Team(TimeStampedModel):
    team_name = models.CharField("Team Name", max_length=255)
    slug = AutoSlugField("Team Address", unique=True, always_update=False, populate_from="team_name")
    created_date = models.DateField("Date Created:", blank=True)
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.team_name

    def get_absolute_url(self):
        return reverse('nba:team_detail', kwargs={"slug": self.slug})

class Match(TimeStampedModel):
    match_name = models.CharField("Match Name", max_length=255)
    slug = AutoSlugField("Match Address", unique=True, always_update=False, populate_from="match_name")
    match_date = models.DateField("Match Date", blank=True)
    team_id1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1', null=True)
    team_id2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2', null=True)
    winner_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='winner', null=True)
    created_date = models.DateField("Date Created:", blank=True)
    
    def __str__(self):
        return self.match_name

class UserTeam(TimeStampedModel):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
	team_name = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
	