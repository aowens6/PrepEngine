from django.shortcuts import render
from .models import TutorSet, Question
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

def createSet(request):
    return render(request, 'tutor_sets/createSet.html')

class TutorSetDetailView(DetailView):
    model = TutorSet

class TutorSetCreateView(LoginRequiredMixin, CreateView):
    model = TutorSet
    fields = ['title',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['prompt']

    def form_valid(self, form):
        form.instance.tutorSet = TutorSet.objects.get(pk=self.kwargs['tutorSetID'])
        return super().form_valid(form)
