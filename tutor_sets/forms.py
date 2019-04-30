from django import forms
from .models import TutorSet, Question, Option

class TutorSetForm(forms.ModelForm):
    class Meta:
        model = TutorSet
        fields = [
            'title',
            'description',
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
    min_num=1,
    fields=('order', 'text', 'correct'),
    formset=OptionFormSet,
)

class QuestionAttemptForm(forms.Form):
    choices = forms.ModelMultipleChoiceField(queryset=Option.objects.none(),
                                             widget=forms.RadioSelect, required=True,                                                        show_hidden_initial=True)

    def __init__(self, question):
        super(QuestionAttemptForm, self).__init__()
        self.fields['choices'].queryset = question.option_set.all()
        self.fields['choices'].empty_label = None
        self.fields['choices'].label = question.prompt


