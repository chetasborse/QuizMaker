from django.shortcuts import render, redirect
from .models import Quiz
import re
from django.views.generic import DetailView, ListView, FormView
from django.contrib.auth.models import User
from creation.models import Questions


def home(request):
    context = {
        'title': 'Home Page',
        'quizes': Quiz.objects.all()
    }
    return render(request, 'quiz/home.html', context)


class HomeListView(ListView):
    model = Quiz
    template_name = 'quiz/home.html'
    context_object_name = 'quizes'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context_entry = "Home"
        context["title"] = new_context_entry
        return context


# class QuizDetailView(DetailView, FormView):
#     model = Quiz
#     template_name = 'quiz/detail.html'
#     form_class = QuizAttempt
#     success_url = 'quiz/home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         new_context_entry = "Details"
#         context["title"] = new_context_entry
#         return context


def quizdetailview(request, pk):
    quiz = Quiz.objects.filter(pk=pk).first()
    # is_error = False
    # if request.method == 'POST':
    #     form = QuizAttempt(request.POST)
    #     if form.is_valid():
    #         password = form.cleaned_data.get('password')
    #         if quiz.password == password:
    #             return redirect('quiz-home')
    #         else:
    #             is_error = True
    # form = QuizAttempt()
    context = {
        'title': 'Details',
        'object': quiz,
        # 'form': form,
        # 'error': is_error
    }
    return render(request, 'quiz/detail.html', context)


def about(request):
    return render(request, 'quiz/about.html', {'title': 'About Page'})


def searchview(request):
    search = request.GET.get('Search', 'default')
    quizes = Quiz.objects.all()
    users = User.objects.all()

    elems = []
    elems2 = []

    for item in quizes:
        if re.search(search, item.title, re.IGNORECASE):
            elems.append(item)
        elif re.search(search, str(item.author), re.IGNORECASE):
            elems.append(item)

    for item in users:
        if re.search(search, item.username, re.IGNORECASE):
            elems2.append(item)

    context = {
        'title': 'Results',
        'quizes': elems,
        'users': elems2
    }
    return render(request, 'quiz/searches.html', context)


def quizpage(request, pk):
    questions = Questions.objects.filter(quiz_no=pk)
    context = {
        'title': 'QuizPage',
        'questions': questions
    }
    return render(request, 'quiz/quizpage.html', context)
