# app/progress/urls.py
from django.urls import path
from . import views

app_name = "progress"

urlpatterns = [
    path("list/", views.progress_list, name="progress_list"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("result/<int:result_id>/", views.lesson_result_detail, name="result_detail"),
]
