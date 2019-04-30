from django.shortcuts import render, get_object_or_404
from .models import TutorSet, Question, Option
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from . import forms

@login_required
@never_cache
def tutorset_create(request):
    form = forms.TutorSetForm

    if request.method == 'POST':
        form = forms.TutorSetForm(request.POST)
        if form.is_valid():
            tutorSet = form.save(commit=False)
            tutorSet.author = request.user
            tutorSet.save()
            form=forms.TutorSetForm
            messages.success(request, 'Tutor set added')
            return HttpResponseRedirect(tutorSet.get_absolute_url())
    return render(request, 'tutor_sets/tutorset_form.html', {'form': form, 'title': 'New Tutor Set'})


@login_required
def tutorset_start(request, tutorset_pk):
    tutorSet = get_object_or_404(TutorSet, pk=tutorset_pk)
    questions_list = list(tutorSet.question_set.all())
    page = request.GET.get('page')
    paginator = Paginator(questions_list, 1)

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'tutor_sets/quiz_attempt.html', {
        'tutorSet': tutorSet,
        'questionSet': questions,
    })


@login_required
def tutorset_edit(request, pk):
    tutorSet = get_object_or_404(TutorSet, pk=pk)
    form = forms.TutorSetForm(instance=tutorSet)
    if request.method == 'POST':
        form = forms.TutorSetForm(instance=tutorSet, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Tutor set updated')
            return HttpResponseRedirect(tutorSet.get_absolute_url())
    return render(request, 'tutor_sets/tutorset_form.html',
                  {'form': form, 'title': 'Edit Tutor Set'})

@login_required
def tutorset_delete(request, tutorset_pk):
    tutorSet = get_object_or_404(TutorSet, pk=tutorset_pk)
    tutorSet.delete()
    messages.success(request, f'Tutor set {tutorSet.title} deleted')
    return HttpResponseRedirect('/')

@login_required
def question_create(request, tutorset_pk):
    tutorSet = get_object_or_404(TutorSet, pk=tutorset_pk)
    form = forms.QuestionForm
    option_forms = forms.OptionInlineFormSet(
        queryset=Option.objects.none()
    )

    if request.method == 'POST':
        form = forms.QuestionForm(request.POST)
        option_forms = forms.OptionInlineFormSet(
            request.POST,
            queryset=Option.objects.none()
        )

        if form.is_valid() and option_forms.is_valid():
            question = form.save(commit=False)
            question.tutorSet = tutorSet
            question.save()

            options = option_forms.save(commit=False)

            for option in options:
                option.question = question
                option.save()

            messages.success(request, 'Added new question')
            return HttpResponseRedirect(tutorSet.get_absolute_url())
    return render(request, 'tutor_sets/question_form.html',
                  {'tutorSet': tutorSet, 'form': form, 'title': 'New Question', 'formset': option_forms})


@login_required
def question_edit(request, tutorset_pk, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    tutorSet = get_object_or_404(TutorSet, pk=tutorset_pk)
    form = forms.QuestionForm(instance=question)
    option_forms = forms.OptionInlineFormSet(
        queryset=form.instance.option_set.all()
    )

    if request.method == 'POST':
        form = forms.QuestionForm(instance=question, data=request.POST)
        option_forms = forms.OptionInlineFormSet(
            request.POST,
            queryset=form.instance.option_set.all()
        )
        if form.is_valid() and option_forms.is_valid():
            form.save()

            options = option_forms.save(commit=False)

            for option in options:
                option.question = question
                option.save()

            for option in option_forms.deleted_objects:
                option.delete()

            messages.success(request, 'Edited question')
            return HttpResponseRedirect(question.get_absolute_url())
    return render(request, 'tutor_sets/question_form.html',
                  {'form': form,
                   'title': 'Edit Question',
                   'tutorSet': tutorSet,
                   'formset': option_forms,
                   'question': question})

@login_required
def question_delete(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    question.delete()
    messages.success(request, f'{question.prompt} deleted')
    return HttpResponseRedirect(question.get_absolute_url())


@login_required
def tutorset_overview(request, tutorset_pk):
    tutorSet = get_object_or_404(TutorSet, pk=tutorset_pk)
    questions_list = tutorSet.question_set.all()
    page = request.GET.get('page')
    paginator = Paginator(questions_list, 5)

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'tutor_sets/tutorset_detail.html', {
        'tutorSet': tutorSet,
        'questionSet': questions,
    })

