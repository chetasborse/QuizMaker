from django.contrib import admin
from .models import Quiz, QuizAnswer, Attempt


class OrderQuiz(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'questions', 'marks', 'date_posted']


admin.site.register(Quiz, OrderQuiz)
admin.site.register(QuizAnswer)
admin.site.register(Attempt)
