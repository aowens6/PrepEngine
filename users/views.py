from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from tutor_sets.models import TutorSet
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html', {'form': form})

def creator_profile(request, creator_pk):
    creator=User.objects.get(pk=creator_pk)
    tutorSets = TutorSet.objects.filter(author=creator)
    return render(request, 'users/creator_profile.html', {'creator': creator, 'tutorSets:': tutorSets})

class CreatorTutorSetListView(ListView):
    model = TutorSet
    template_name = 'users/creator_profile.html'
    context_object_name = 'tutorSets'
    paginate_by = 5

    def get_queryset(self):
        creator = get_object_or_404(User, pk=self.kwargs.get('creator_pk'))
        return TutorSet.objects.filter(author=creator)

    def get_context_data(self, **kwargs):
        creator = get_object_or_404(User, pk=self.kwargs.get('creator_pk'))
        context = super(CreatorTutorSetListView, self).get_context_data(**kwargs)
        context['creator'] = creator
        return context
