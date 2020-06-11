from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from users import views as user_views
from .views import QuizDetailView, HomeListView
from users.views import UserProfiles

urlpatterns = [
    path('', HomeListView.as_view(), name='quiz-home'),
    path('quiz/<int:pk>/', QuizDetailView.as_view(), name='quiz_detail'),
    path('userprofiles/<int:pk>/', UserProfiles.as_view(), name='user_details'),
    path('about/', views.about, name='quiz-about'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('searches/', views.searchview, name='searches'),
    path('profile/', user_views.myprofile, name='profile'),
]
