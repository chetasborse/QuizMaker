from django import forms

CHOICES = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
)


class QuestionForm(forms.Form):
    question = forms.CharField()
    option_a = forms.CharField()
    option_b = forms.CharField()
    option_c = forms.CharField()
    option_d = forms.CharField()
    answer = forms.ChoiceField(choices=CHOICES)
    marks = forms.IntegerField()