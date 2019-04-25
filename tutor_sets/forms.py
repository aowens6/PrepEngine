from django import forms
from .models import TutorSet, Question, Option

class TutorSetForm(forms.ModelForm):
    class Meta:
        model = TutorSet
        fields = [
            'title',
            'totalQuestions',
        ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'prompt',
            'order',
            'shuffle_answers',
        ]


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = [
            'order',
            'text',
            'correct',
        ]

OptionFormSet = forms.modelformset_factory(Option, form=OptionForm)

OptionInlineFormSet = forms.inlineformset_factory(
    Question,
    Option,
    fields=('order', 'text', 'correct'),
    formset=OptionFormSet,
)