from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

class Team(TimeStampedModel):
    team_name = models.CharField("Team Name", max_length=255)
    slug = AutoSlugField("Team Address", unique=True, always_update=False, populate_from="team_name")
    created_date = models.DateField("Date Created:", blank=True)
    
    def __str__(self):
        return self.team_name
