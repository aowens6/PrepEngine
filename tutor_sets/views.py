from django.shortcuts import render
from .models import TutorSet
from django.views.generic import DetailView

def createEngine(request):
    return render(request, 'tutor_sets/createEngine.html')

class TutorSetDetailView(DetailView):
    model = TutorSet