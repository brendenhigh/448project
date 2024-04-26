from django.core.management.base import BaseCommand
from everycheese.nba.models import Match, Team

class Command(BaseCommand):
    """Put an example of running this command in this comment so you can
    copy/paste to terminal later.

    Example:
    ./manage.py inspection
    """

    help = './manage.py inspection --help will print this out'

    def add_arguments(self, parser):
        """Setup arguments.

        See here https://docs.python.org/3/library/argparse.html
        """


    def handle(self, *args, **options):
 

        
        # Logic to update team points based on match winner
        matches = Match.objects.filter(winner_id__isnull=False)
        for match in matches:
            winning_team = match.winner_id
            if winning_team:
                # Add 3 points to the winning team
                winning_team.points += 3
                winning_team.save()