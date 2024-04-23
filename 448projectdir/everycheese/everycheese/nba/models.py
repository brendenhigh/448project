from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from django.urls import reverse
from django.conf import settings


class Team(TimeStampedModel):
    team_name = models.CharField("Team Name", max_length=255)
    slug = AutoSlugField("Team Address", unique=True, always_update=False, populate_from="team_name")
    created_date = models.DateField("Date Created:", blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    
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
    team1_assists = models.IntegerField("Team 1 Assists", null=True)
    team2_assists = models.IntegerField("Team 2 Assists", default=0)
    team1_rebounds = models.IntegerField("Team 1 Rebounds", default=0)
    team2_rebounds = models.IntegerField("Team 2 Rebounds", default=0)
    team1_shooting = models.IntegerField("Team 1 Shooting", default=0)
    team2_shooting = models.IntegerField("Team 2 Shooting", default=0)
    score = models.CharField("Score", max_length=255, blank=True, null=True)
    

    
    def __str__(self):
        return self.match_name

class UserTeam(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, related_name='user_teams')
    slug = AutoSlugField("UserTeam Address", unique=True, always_update=False, populate_from="user")

