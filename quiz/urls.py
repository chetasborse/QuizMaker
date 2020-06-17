from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from users import views as user_views
from .views import HomeListView
from users.views import UserProfiles
from creation import views as create_views

urlpatterns = [
    path('', HomeListView.as_view(), name='quiz-home'),
    # path('quiz/<int:pk>/', QuizDetailView.as_view(), name='quiz_detail'),
    path('quiz/<int:pk>/', views.quizdetailview, name='quiz_detail'),
    path('quizview/<int:pk>/<int:times>/<str:password>/', create_views.quizview, name='quiz_view'),
    path('userprofiles/<int:pk>/', UserProfiles.as_view(), name='user_details'),
    path('about/', views.about, name='quiz-about'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('searches/', views.searchview, name='searches'),
    path('profile/', user_views.myprofile, name='profile'),
    path('response/<int:pk>/', user_views.responses, name='responses'),
    path('review/<int:pk>/<str:authors>/', create_views.review, name='review'),
    path('quizpage/<int:pk>/', views.quizpage, name='quizpage'),
]
