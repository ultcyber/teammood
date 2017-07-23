from django.db import models

# Create your models here.
class Mood(models.Model):
    uid = models.CharField(max_length=200)
    date_requested = models.DateField
    answered = models.BooleanField
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

class Team(models.Model):
    # ......
    pass



