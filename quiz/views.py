from django.shortcuts import render
from .models import Quiz
import re
from django.views.generic import DetailView, ListView
from django.contrib.auth.models import User


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


class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'quiz/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_context_entry = "Details"
        context["title"] = new_context_entry
        return context


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
