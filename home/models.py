from django.db import models
from django.contrib.auth.models import User

class TutorSet(models.Model):
    title = models.CharField(max_length=100)
    score = models.IntegerField()
    totalQuestions = models.IntegerField()
