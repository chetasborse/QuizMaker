from django.db import models
from django.contrib.auth.models import User

CHOICES = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
)


class Questions(models.Model):
    quiz_no = models.IntegerField()
    question = models.CharField(max_length=250)
    option_a = models.CharField(max_length=50)
    option_b = models.CharField(max_length=50)
    option_c = models.CharField(max_length=50)
    option_d = models.CharField(max_length=50)
    answer = models.CharField(choices=CHOICES, default="A", max_length=10)
    marks = models.IntegerField()

    def __str__(self):
        return self.question
