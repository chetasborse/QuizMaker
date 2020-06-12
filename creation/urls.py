from django.urls import path
from . import views
from .views import QuizCreateView

urlpatterns = [
    path('', QuizCreateView.as_view(), name='create_home'),
]