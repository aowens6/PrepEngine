from django.shortcuts import render
from .models import TutorSet, Question
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView

def createSet(request):
    return render(request, 'tutor_sets/createSet.html')

class TutorSetDetailView(DetailView):
    model = TutorSet


@login_required
class TutorSetCreateView(CreateView):
    model = TutorSet
    fields = ['title',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def QuestionCreateView(CreateView):
    model = Question
    fields = []