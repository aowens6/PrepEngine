from django.shortcuts import render, get_object_or_404
from tutor_sets.models import TutorSet, Attempt
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

def home(request):
    context = {
        'tutorSets' : TutorSet.objects.all()
    }
    return render(request, 'home/home.html', context)

class TutorSetListView(ListView):
    model = TutorSet
    template_name = 'home/home.html'
    context_object_name = 'tutorSets'
    paginate_by = 5


class UserTutorSetListView(ListView):
    model = TutorSet
    template_name = 'home/user_tutorsets.html'
    context_object_name = 'tutorSets'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return TutorSet.objects.filter(author=user)


class UserAttemptsListView(ListView):
    model = Attempt
    template_name = 'home/user_attempts.html'
    context_object_name = 'attempts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Attempt.objects.filter(user=user)

