from django.urls import path
from . import views

app_name = "lessons"

urlpatterns = [
    # All lessons list
    path("", views.lesson_list, name="lesson_list"),
    # Single lesson detail
    # path("<int:lesson_id>/", views.lesson_detail, name="lesson_detail"),
    # Lesson quiz
    path("<int:lesson_id>/quiz/", views.lesson_quiz, name="lesson_quiz"),
    # lesson detail
    path("content/<slug:course_slug>/<str:lesson_filename>/", views.lesson_detail, name="lesson_detail"),
path('<slug:course_slug>/<slug:lesson_slug>/', views.start_lesson, name='start_lesson'),
    # path("<slug:course_slug>/<str:lesson_filename>/", views.lesson_detail, name="lesson_detail"),
    # lesson progress
    path("<slug:course_slug>/<str:lesson_filename>/progress/", views.lesson_progress, name="lesson_progress"),
    # Lesson comments
    path("<int:lesson_id>/comments/", views.lesson_comments, name="lesson_comments"),
    # Lesson resources
    path("<int:lesson_id>/resources/", views.lesson_resources, name="lesson_resources"),
    # Lesson feedback
    path("<int:lesson_id>/feedback/", views.lesson_feedback, name="lesson_feedback"),
]