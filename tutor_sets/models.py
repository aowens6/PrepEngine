from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class TutorSet(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tutorSet-detail', kwargs={'tutorset_pk': self.pk})


class Question(models.Model):
    tutorSet = models.ForeignKey(TutorSet, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    prompt = models.CharField(max_length=255)
    shuffle_answers = models.BooleanField(default=False)
    explanation = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.prompt

    def get_absolute_url(self):
        return self.tutorSet.get_absolute_url()


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    text = models.CharField(max_length=255, default='')
    correct = models.BooleanField(default=False)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.text
