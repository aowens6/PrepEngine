from django.shortcuts import get_object_or_404
from tutor_sets.models import TutorSet, Attempt
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
            return TutorSet.objects.filter(Q(title__icontains=search_term)|Q(author__username__icontains=search_term))
        return TutorSet.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TutorSetListView, self).get_context_data(**kwargs)
        context['search_term'] = self.request.GET['search']
        return context


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

