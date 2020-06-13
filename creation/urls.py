from django.urls import path
from . import views
from .views import QuizCreateView, quiz_create_ques

urlpatterns = [
    path('', QuizCreateView.as_view(), name='create_home'),
    path('questions/<int:pk>/', quiz_create_ques, name='quiz_create_view'),
]