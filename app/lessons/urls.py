# app/lessons/urls.py
from django.urls import path
from . import views

app_name = 'lessons'

urlpatterns = [
    path('', views.lesson_list, name='lesson_list'),
    path('<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('<int:lesson_id>/quiz/', views.lesson_quiz, name='lesson_quiz'),
    path('<int:lesson_id>/progress/', views.lesson_progress, name='lesson_progress'),
    path('<int:lesson_id>/comments/', views.lesson_comments, name='lesson_comments'),
    path('<int:lesson_id>/resources/', views.lesson_resources, name='lesson_resources'),
    path('<int:lesson_id>/feedback/', views.lesson_feedback, name='lesson_feedback'),
]
