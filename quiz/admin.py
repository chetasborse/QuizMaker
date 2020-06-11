from django.contrib import admin
from .models import Quiz


class OrderQuiz(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'questions', 'marks', 'date_posted']


admin.site.register(Quiz, OrderQuiz)
