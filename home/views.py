from django.shortcuts import render
from .models import TutorSet

def home(request):
    context = {
        'tutorSets' : TutorSet.objects.all()
    }
    return render(request, 'home/base.html', context)
