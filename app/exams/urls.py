# app/exams/urls.py
from django.urls import path
from . import views

app_name = 'exams'

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('<int:exam_id>/', views.exam_detail, name='exam_detail'),
    path('<int:exam_id>/quiz/', views.exam_quiz, name='exam_quiz'),
    path('<int:exam_id>/results/', views.exam_results, name='exam_results'),
    path('progress/', views.exam_progress, name='exam_progress'),
    path('notifications/', views.exam_notifications, name='exam_notifications'),
    path('<int:exam_id>/feedback/', views.exam_feedback, name='exam_feedback'),
]
