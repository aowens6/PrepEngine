from django.shortcuts import render
from tutor_sets.models import TutorSet
from django.views.generic import ListView, DetailView

def home(request):
    context = {
        'tutorSets' : TutorSet.objects.all()
    }
    return render(request, 'home/home.html', context)

class TutorSetListView(ListView):
    model = TutorSet
    template_name = 'home/home.html'
    context_object_name = 'tutorSets'


class TutorSetDetailView(DetailView):
    model = TutorSet