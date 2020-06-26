from django.shortcuts import render, redirect
from django.views.generic import CreateView
from quiz.models import Quiz, QuizAnswer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from .forms import QuestionForm, AnswerForm
from .models import Questions, Answers
from django.contrib import messages
from datetime import datetime


class QuizCreateView(LoginRequiredMixin, CreateView):
    model = Quiz
    fields = ['title', 'description', 'questions', 'minutes', 'instructions', 'password']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     quiz = self.get_object()
    #     if self.request.user == quiz.author:
    #         return True
    #     return False


@login_required
def quiz_create_ques(request, pk):
    Q = Quiz.objects.filter(pk=pk)
    quiz = Q.first()
    if request.user == quiz.author:
        QuestionFormSet = formset_factory(QuestionForm, extra=quiz.questions, max_num=quiz.questions)
        if request.method == 'POST':
            formset = QuestionFormSet(request.POST)
            if formset.is_valid():
                q_marks = 0
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
                    q_marks = q_marks + ques.marks
                    ques.save()
                    Q.update(marks=q_marks)
                return redirect('quiz-home')
        else:
            formset = QuestionFormSet
            context = {
                'title': 'lol',
                'formset': formset
            }
        return render(request, 'creation/quiz_create_ques.html', {'form': formset})
    else:
        return redirect('quiz-home')


def quizview(request, pk, times, password):
    questions = Questions.objects.filter(quiz_no=pk)
    quizanswer = QuizAnswer.objects.get(quiz_no=pk, author=request.user)
    print("here1")
    count = len(questions)
    print("here2")
    AnswerFormSet = formset_factory(AnswerForm, extra=count, max_num=count)
    print("here3")
    if request.method == 'POST':
        print("Entered Post")
        formset = AnswerFormSet(request.POST)
        if formset.is_valid():
            mark = 0
            for i, form in enumerate(formset):
                ans = Answers()
                ans.quiz_no = pk
                # remember to check the emptiness of answerfield
                ans.answer = form.cleaned_data.get('answer')
                ans.question_no = questions[i].pk
                ans.author = request.user
                if ans.answer == questions[i].answer:
                    mark = mark + questions[i].marks
                ans.save()
            quizanswer.marks = mark
            quizanswer.save()
            return redirect('profile')
    else:
        formset = AnswerFormSet()
    print("here4")
    mylist = zip(formset, questions)
    print("here")
    # for item1, item2 in mylist:
    #     print(item2)
    #     print(item1)
    context = {
        'title': 'Quiz View',
        'mylist': mylist,
        'form': formset,
        'time': times,
    }
    # return redirect('quiz-home')
    return render(request, 'creation/quizview.html', context)


def review(request, pk, authors):
    if authors == '100':
        answers = Answers.objects.filter(quiz_no=pk, author=request.user)
        quiz_ans = QuizAnswer.objects.filter(quiz_no=pk, author=request.user).first()
    else:
        pkey = int(authors)
        quiz_ans = QuizAnswer.objects.filter(pk=pkey).first()
        answers = Answers.objects.filter(quiz_no=pk, author=quiz_ans.author)
        quiz_ans = QuizAnswer.objects.filter(quiz_no=pk, author=quiz_ans.author).first()
    questions = Questions.objects.filter(quiz_no=pk)

    mylist = zip(questions, answers)
    context = {
        'title': 'Review',
        'mylist': mylist,
        'quiz_ans': quiz_ans
    }
    return render(request, 'creation/review.html', context)


# def likes(request):
#     if request.method == 'POST':
#         id = request.POST['id']