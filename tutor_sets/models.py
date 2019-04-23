from django.db import models
from django.urls import reverse
from django.shortcuts import redirect

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

    # def get_absolute_url(self):
    #     return redirect('')

class Question(models.Model):
    tutorSetID = models.ForeignKey(TutorSet, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question

class Answer(models.Model):
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.answer
