from django import forms


class QuestionForm(forms.Form):
    answers = forms.MultipleChoiceField(label='', widget=forms.CheckboxSelectMultiple())

    def __init__(self, question, *args, **kwargs):
        self.question = question
        answers = self.question.answer_set.all()
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['answers'].choices = [(i.pk, i.name) for i in answers]
