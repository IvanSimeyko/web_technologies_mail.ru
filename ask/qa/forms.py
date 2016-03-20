from django import forms
from models import Question, Answer
from django.contrib.auth.models import User


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    #	question_id = forms.IntegerField(widget=forms.HiddenInput)
    question_id = forms.IntegerField()

    _user = User

    def clean_text(self):
        if self.cleaned_data['text'] == "":
            raise forms.ValidationError("Text is empty", code='empty')
        return self.cleaned_data['text']

    def save(self):
        # won't be there if no question, no check
        qst = Question.objects.get(pk=self.cleaned_data['question_id'])
        return Answer.objects.create(
                    question=qst,
                    text=self.cleaned_data['text'],
                    author=self._user)