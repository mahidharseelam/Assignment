from django.db import models

# Create your models here.
class Contests(models.Model):
    contest_id=models.IntegerField()
    hacker_id=models.IntegerField()
    name=models.CharField(max_length=30)

class Colleges(models.Model):
    college_id=models.IntegerField()
    contest_id=models.IntegerField()

class Challenges(models.Model):
    challenge_id=models.IntegerField()
    college_id=models.IntegerField()

class View_Stats(models.Model):
    challenge_id=models.IntegerField()
    total_views=models.IntegerField()
    total_unique_views=models.IntegerField()

class Submission_Stats(models.Model):
    challenge_id=models.IntegerField()
    total_submission=models.IntegerField()
    total_accepted_submissions=models.IntegerField()
