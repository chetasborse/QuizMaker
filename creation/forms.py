from django import forms

CHOICES = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
)


class QuestionForm(forms.Form):
    question = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the question'}))
    option_a = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option A'}))
    option_b = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option B'}))
    option_c = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option C'}))
    option_d = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option D'}))
    answer = forms.ChoiceField(choices=CHOICES)
    marks = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Marks'}))


class AnswerForm(forms.Form):
    answer = forms.ChoiceField(choices=CHOICES)

class QuizAttempt(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
