from django.db import models

class TutorSet(models.Model):
    title = models.CharField(max_length=100)
    score = models.IntegerField()
    totalQuestions = models.IntegerField()