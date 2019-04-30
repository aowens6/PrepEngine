from django.shortcuts import get_object_or_404
from tutor_sets.models import TutorSet
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.db.models import Q


class TutorSetListView(ListView):
    model = TutorSet
    template_name = 'home/home.html'
    context_object_name = 'tutorSets'
    paginate_by = 5

    def get_queryset(self):
        if 'search' in self.request.GET:
            search_term = self.request.GET['search']
            return TutorSet.objects.filter(
                            Q(title__icontains=search_term)|
                            Q(author__username__icontains=search_term)|
                            Q(description__icontains=search_term))
        return TutorSet.objects.all()


class UserTutorSetListView(ListView):
    model = TutorSet
    template_name = 'home/user_tutorsets.html'
    context_object_name = 'tutorSets'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return TutorSet.objects.filter(author=user)

class ReportListView(ListView):
    model = TutorSet
    template_name = 'home/reports.html'
    context_object_name = 'tutorSets'
    paginate_by = 5

    def get_queryset(self):
        if 'search' in self.request.GET:
            search_term = self.request.GET['search']
            return TutorSet.objects.filter(
                            Q(title__icontains=search_term)|
                            Q(author__username__icontains=search_term)|
                            Q(description__icontains=search_term))
        return TutorSet.objects.all()

