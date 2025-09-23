# app/exams/urls.py
from django.urls import path
from . import views

app_name = "exams"

urlpatterns = [
    path("list/", views.exam_list, name="exam_list"),
    path("<int:id>/", views.exam_detail, name="exam_detail"),
]
