from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

class TutorSet(models.Model):
    title = models.CharField(max_length=100)
    score = models.PositiveIntegerField(default=0)
    totalQuestions = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tutorSet-detail', kwargs={'pk': self.pk})

class Question(models.Model):
    tutorSet = models.ForeignKey(TutorSet, on_delete=models.CASCADE)
    prompt = models.CharField(max_length=255)

    def __str__(self):
        return self.prompt

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
