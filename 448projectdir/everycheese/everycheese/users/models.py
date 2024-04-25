from django.contrib.auth.models import AbstractUser
from everycheese.nba.models import Team
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name Do Not Cover Name Patterns
    # Around the Globe.
    name = models.CharField(
        _("Name of User"), blank=True, max_length=255
    )


    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    
    slug = AutoSlugField("User Address", unique=True, always_update=False, populate_from="name", null=True)

    def get_absolute_url(self):
        return reverse(
            "users:detail", kwargs={"username": self.username}
        )

