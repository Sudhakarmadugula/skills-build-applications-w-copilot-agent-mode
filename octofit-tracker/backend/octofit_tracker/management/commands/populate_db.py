from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):

        User = get_user_model()
        Team = octo_models.Team
        Activity = octo_models.Activity
        Leaderboard = octo_models.Leaderboard
        Workout = octo_models.Workout

        # Clear all collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', team=marvel),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='pass', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='pass', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', password='pass', team=dc),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='pass', team=dc),
        ]

        # Create Activities
        activities = [
            Activity.objects.create(user=users[0], type='run', duration=30, distance=5),
            Activity.objects.create(user=users[1], type='cycle', duration=60, distance=20),
            Activity.objects.create(user=users[2], type='swim', duration=45, distance=2),
            Activity.objects.create(user=users[3], type='run', duration=25, distance=4),
            Activity.objects.create(user=users[4], type='cycle', duration=70, distance=25),
            Activity.objects.create(user=users[5], type='swim', duration=50, distance=3),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Morning Cardio', description='Cardio session for superheroes'),
            Workout.objects.create(name='Strength Training', description='Strength session for superheroes'),
        ]

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

# Models for reference (should be in octofit_tracker/models.py):
# class Team(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#
# class Activity(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     type = models.CharField(max_length=50)
#     duration = models.IntegerField()
#     distance = models.FloatField()
#
# class Workout(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#
# class Leaderboard(models.Model):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     points = models.IntegerField()
