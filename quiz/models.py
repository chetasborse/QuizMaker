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

    def get_absolute_url(self):
        return reverse('quiz_detail', kwargs={'pk': self.pk})
