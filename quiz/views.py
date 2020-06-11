from django.shortcuts import render
from .models import Quiz
import re


def home(request):
    context = {
        'title': 'Home Page',
        'quizes': Quiz.objects.all()
    }
    return render(request, 'quiz/home.html', context)


def about(request):
    return render(request, 'quiz/about.html', {'title': 'About Page'})


def searchview(request):
    search = request.GET.get('Search', 'default')
    quizes = Quiz.objects.all()

    elems = []

    for item in quizes:
        if re.search(search, item.title, re.IGNORECASE):
            elems.append(item)
        elif re.search(search, str(item.author), re.IGNORECASE):
            elems.append(item)

    context = {
        'title': 'Results',
        'quizes': elems
    }
    return render(request, 'quiz/searches.html', context)
