from django.db import models
from django.utils import timezone

# Create your models here.
class Mood(models.Model):
    uid = models.CharField(max_length=100)
    date_requested = models.DateField(("Date"), default=timezone.datetime.now)
    answered = models.BooleanField(default=False)
    team = models.ForeignKey("Team", on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)

class Team(models.Model):
    name = models.CharField(max_length=100)


