from django.shortcuts import render
from django.views.generic import CreateView
from quiz.models import Quiz
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from .forms import QuestionForm
from .models import Questions


class QuizCreateView(LoginRequiredMixin, CreateView):
    model = Quiz
    fields = ['title', 'description', 'questions', 'marks', 'instructions']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def quiz_create_ques(request, pk):
    quiz = Quiz.objects.filter(pk=pk).first()
    QuestionFormSet = formset_factory(QuestionForm, extra=quiz.questions, max_num=quiz.questions)
    if request.method == 'POST':
        formset = QuestionFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                ques = Questions()
                ques.quiz_no = pk
                ques.question = form.cleaned_data.get('question')
                ques.option_a = form.cleaned_data.get('option_a')
                ques.option_b = form.cleaned_data.get('option_b')
                ques.option_c = form.cleaned_data.get('option_c')
                ques.option_d = form.cleaned_data.get('option_d')
                ques.answer = form.cleaned_data.get('answer')
                ques.marks = form.cleaned_data.get('marks')
                ques.save()
            return render(request, 'quiz/about.html', {'title': 'About Page'})
    else:
        formset = QuestionFormSet
        context = {
            'title': 'lol',
            'formset': formset
        }
    return render(request, 'creation/quiz_create_ques.html', {'form': formset})

