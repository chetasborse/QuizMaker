from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Quiz(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(default=None)
    instructions = models.TextField(default=None)
    questions = models.IntegerField()
    marks = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=20, default=None)
    hours = models.IntegerField(default=0)
    minutes = models.IntegerField(default=30)

    def get_absolute_url(self):
        return reverse('quiz_create_view', kwargs={'pk': self.pk})


class QuizAnswer(models.Model):
    quiz_no = models.IntegerField()
    questions = models.IntegerField(default=0)
    marks = models.IntegerField(default=0)
    total_marks = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    title = models.CharField(max_length=50, default='')
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="host", default=None)


class Attempt(models.Model):
    quiz_no = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)